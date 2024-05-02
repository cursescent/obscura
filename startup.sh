source python_virtual/bin/activate
python app/manage.py makemigrations index
python app/manage.py migrate
python app/manage.py runserver
deactivate
