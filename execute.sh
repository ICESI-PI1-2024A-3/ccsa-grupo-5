virtualenv venv
.\venv\Scripts\activate
pip install django
pip install coverage
pip install selenium
pip install swapper
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
