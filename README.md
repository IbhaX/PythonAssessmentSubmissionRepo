# Python Assessment Submission Repo

This is a Django web application that retrieves analytic reports about a searched GitHub repository.

## Setup

1. Clone the repository:

  ```bash
    git clone https://github.com/your-username/PythonAssessmentSubmissionRepo.git
  ```


2. Navigate to the project directory:

  ```bash
    cd PythonAssessmentSubmissionRepo
  ```


3. Create a virtual environment and activate it:

  ```python
    python3 -m venv env
  ```
  `source env/bin/activate` for linux and mac  # On Windows, use `env\Scripts\activate`


4. Install the required dependencies:

  ```bash
    pip install -r requirements.txt
  ```


5. Apply the database migrations:

  ```bash
    python manage.py migrate
  ```


6. Create a superuser account:

  ```bash
    python manage.py createsuperuser
  ```


## Running the Application

1. Start the development server:

  ```bash
    python manage.py runserver
  ```


2. Open your web browser and navigate to `http://localhost:8000` to access the application.


## Running with Docker

1. Make sure you have Docker installed on your system. You can download and install Docker from [here](https://www.docker.com/get-started).

2. Build the Docker image for the application:

   ```bash
   docker build -t python-assessment .
   ```

3. Once the image is built successfully, you can run the Docker container:

   ```bash
   docker run -p 8000:8000 python-assessment
   ```

   This command maps port 8000 of the Docker container to port 8000 of your local machine. Adjust the port mapping if necessary.

4. Open your web browser and navigate to `http://localhost:8000` to access the application running inside the Docker container.

## Usage

1. Sign up for a new account or log in with your existing credentials.
2. Enter the name of a GitHub repository in the search field (e.g., `django`).
3. The application will fetch and display analytic reports for the specified repository.
