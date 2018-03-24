To run:
    
    git clone https://github.com/hs3city/hs-library-back.git
    
    cd hs-library-back
    
    virtualenv -p python3 venv
        
    . venv/bin/activate
    
    python manage.py migrate
    
    python manage.py runserver

To create admin user for test. 
    
    python manage.py createsuperuser

To run:

    python manage.py runserver

Endpoints with docs:

    - Books endpoint docs:
    http://127.0.0.1:8000/api-v1/book/
    
    - Tags endpoint docs:
    http://127.0.0.1:8000/api-v1/tag/
    
    - Users endpoint docs:
    http://127.0.0.1:8000/api-v1/user/
    