Clone the repository with the application.

Create a virtual environment
python -m venv venv

Run the virtual environment

Set all dependencies from requirements.txt
pip install -r requirements.txt

Make Migration models
python manage.py makemigrations.

Apply migration
python manage.py migrate.

Run the server
python manage.py runserver

Use 