Setup
1- The first thing to do is to clone the repository:
  - git clone https://github.com/himarajab/vending_machine
  - cd vending_machine
2-Create a virtual environment :
  - virtualenv venv
4-Activate the virtual environment :
  - source venv/bin/activate
  
5- Install dependencies:
  - pip install -r requirements.txt
6- run tests:
  - pytest
7- Run the application:
  python manage.py makemigrations
  python manage.py migrate
  python manage.py runserver
And navigate to http://127.0.0.1:8000/swagger/
