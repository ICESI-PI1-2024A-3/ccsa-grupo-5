virtualenv venv
.\venv\Scripts\activate
pip install django
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
