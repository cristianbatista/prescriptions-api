# prescriptions-api

[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)

Application responsible for prescriptions registrations


### prerequisites ###

- [python 3.8.2+](https://www.python.org/downloads/release/python-386/) 
- [docker-compose](https://docs.docker.com/compose/install/)

### setup development ###

1. Creates virtualenv and install the dependencies:

        make install

2. Create database 

        make infra-up

3. Set environment variables

        ENV=development
        POSTGRE_URL=postgresql+psycopg2://usr_prescription:secret@localhost:5432/prescription_db
        PATIENTS_API_URL=https://url/v1
        PATIENTS_API_TOKEN_AUTH="Bearer token"
        PATIENTS_API_MAX_RETRY=2
        PATIENTS_API_TIMEMOUT=3
        PHYSICIANS_API_URL=https://url/v1
        PHYSICIANS_API_TOKEN_AUTH="Bearer token"
        PHYSICIANS_API_MAX_RETRY=2
        PHYSICIANS_API_TIMEMOUT=4
        CLINICS_API_URL=https://url/v1
        CLINICS_API_TOKEN_AUTH="Bearer token"
        CLINICS_API_MAX_RETRY=5
        CLINICS_API_TIMEMOUT=5
        METRICS_API_URL=https://url/v1
        METRICS_API_TOKEN_AUTH="Bearer token"
        METRICS_API_MAX_RETRY=5
        METRICS_API_TIMEMOUT=5

4. Run debug api

        make debug-api
        

5. API docs

        http://localhost:8000/docs

6. Run unit tests
 
        make tests
        
7. Run coverage code

        make coverage       


### continuous integration ###

1. The project use github workflows for build and unit tests
        
        # .github/workflows/python-app.yml
        https://github.com/cristianbatista/prescriptions-api/actions
        

### continuous deployment ###

1. The API is published on the heroku platform. Every commit on the main branch is deployed        

        # link api heroku plataform
        https://prescriptions-api-challenge.herokuapp.com/docs