# Python Assessment Submission Repo

This is a Django web application that retrieves analytic reports about a searched GitHub repository.

## Setup

1. Clone the repository:

git clone https://github.com/your-username/PythonAssessmentSubmissionRepo.git


2. Navigate to the project directory:

cd PythonAssessmentSubmissionRepo


3. Create a virtual environment and activate it:

python3 -m venv env
source env/bin/activate  # On Windows, use `env\Scripts\activate`


4. Install the required dependencies:

pip install -r requirements.txt


5. Apply the database migrations:

python manage.py migrate


6. Create a superuser account:

python manage.py createsuperuser


## Running the Application

1. Start the development server:

python manage.py runserver


2. Open your web browser and navigate to `http://localhost:8000` to access the application.

## Usage

1. Sign up for a new account or log in with your existing credentials.
2. Enter the name of a GitHub repository in the search field (e.g., `django/django`).
3. Click the "Get Analytics" button.
4. The application will fetch and display analytic reports for the specified repository.
