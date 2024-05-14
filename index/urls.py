from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name="home"),
    path('login/', views.LoginView.as_view(), name="login"),
    path('logout/', views.LogoutView.as_view(), name="logout"),
    path('signup/', views.SignUpView.as_view(), name="signup"),    
    
    path('password_reset/', views.CustomPasswordResetFormView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name="index/recovery/password_reset_done.html"), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', views.CustomPasswordResetConfirmView.as_view(template_name="index/recovery/password_reset_confirm.html"), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name="index/recovery/password_reset_complete.html"), name='password_reset_complete'),
    
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('search-repo/', views.SearchRepoView.as_view(), name='search-repo'),
    path('repo/<str:username>/<str:repo_name>/', views.RepoDetailsView.as_view(), name='repo-details'),
]
