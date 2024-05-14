from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import FormView, TemplateView
from django.db import IntegrityError
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db import transaction

from index.forms import CustomSetPasswordForm, SignUpForm, ProfileForm, CustomPasswordResetForm, LoginForm
from index.models import Profile, SearchHistory, RepoDetails
from index.utils.GithubApi import GitHubAPI




class HomeView(LoginRequiredMixin, TemplateView):
    template_name = "index/home.html"
    login_url = reverse_lazy("login")

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


class SearchRepoView(View):
    def post(self, request):
        search = request.POST.get("search")
        
        initial_search = SearchHistory.objects.filter(user=request.user, search_term=search)
        if initial_search.exists():
            results = []
            for repo in initial_search.all():
                results.extend(repo.repositories.all())
        else:        
            client = GitHubAPI()
            results = client.search_repo_by_name(search)
            
            with transaction.atomic():
                history = SearchHistory.objects.create(
                    user=request.user,
                    search_term=search
                )
                for repo in results:
                    saved_repo, _ = RepoDetails.objects.get_or_create(
                        repo_name=repo.get("name"),
                        repo_description=repo.get("description"),
                        repo_url=repo.get("html_url"),
                        repo_owner=repo.get("owner").get("username")
                    )
                    history.repositories.add(saved_repo.id) 
            results = history.repositories.all()
        
        paginator = Paginator(results, 10) 
        page = request.GET.get('page')
        try:
            paginated_results = paginator.page(page)
        except PageNotAnInteger:
            paginated_results = paginator.page(1)
        except EmptyPage:
            paginated_results = paginator.page(paginator.num_pages)
        
        return render(request, "index/repo-list.html", {"results": paginated_results})




class RepoDetailsView(View):
    def get(self, request, username, repo_name):
        client = GitHubAPI()
        result = client.get_repo_details(username, repo_name)
        return render(request, "index/repo-details.html", {"repo": result})


class LoginView(FormView):
    template_name = 'index/login.html'
    form_class = LoginForm

    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(self.request, username=username, password=password)
        if user:
            login(self.request, user)
            messages.success(self.request, "Successfully Logged in")
            return redirect("home")
        else:
            form.add_error('username', 'Invalid username or password.')
            return self.form_invalid(form)


class LogoutView(View):
    def get(self, request):
        if request.user.is_authenticated:
            logout(request)
            messages.success(request, "Successfully logged out!!")
        return redirect("home")


class SignUpView(FormView):
    template_name = "index/signup.html"
    form_class = SignUpForm

    def form_valid(self, form):
        try:
            user = form.save()
            _, created = Profile.objects.get_or_create(user=user)
            if created:
                messages.success(self.request, "Signup Successful")
            login(self.request, user)
            return redirect("home")
        except IntegrityError:
            messages.error(self.request, "Error creating user profile. Please try again.")
            return self.form_invalid(form)


class ProfileView(View):
    template_name = 'index/profile.html'

    def get(self, request):
        form = ProfileForm(instance=request.user.profile)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
        return render(request, self.template_name, {'form': form})


class CustomPasswordResetConfirmView(FormView):
    form_class = CustomSetPasswordForm
    success_url = reverse_lazy('password_reset')
    template_name = 'index/recovery/password_reset_form.html'

    def form_valid(self, form):
        password1 = form.cleaned_data.get('new_password1')
        password2 = form.cleaned_data.get('new_password2')
        if password1 == password2:
            user = form.save()
            login(self.request, user)
            messages.success(self.request, 'Password reset successfully.')
            return super().form_valid(form)
        else:
            messages.error(self.request, 'Passwords do not match.')
            return self.form_invalid(form)


class CustomPasswordResetFormView(FormView):
    form_class = CustomPasswordResetForm
    success_url = reverse_lazy('password_reset_done')
    template_name = 'index/recovery/password_reset_form.html'

    def form_valid(self, form):
        messages.success(self.request, 'Password reset email sent successfully.')
        return super().form_valid(form)

    def form_invalid(self, form):
        return render(self.request, self.template_name, {'form': form})
