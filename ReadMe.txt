--backend
pip install djangorestframework
pip install react-dom
mkdir django
cd django
mkdir todo
cd todo
mkdir backend
cd backend
django-admin startproject todo_project
cd todo_project
python manage.py startapp todos
python manage.py runserver
python manage.py migrate
python manage.py makemigrations todos
python manage.py sqlmigrate todos 0001
python manage.py createsuperuser

python manage.py runserver


--frontend
cd django
mkdir frontend
cd frontend
npm install -g create-react-app
create-react-app frontend
cd frontend 
npm start


