virtualenv venv
source venv/bin/activate
pip3 install django
pip3 install coverage
pip3 install selenium
pip3 install -r requirements.txt
python3 manage.py makemigrations
python3 manage.py migrate
