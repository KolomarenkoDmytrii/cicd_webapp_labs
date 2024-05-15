# cicd_webapp_labs
CI/CD web-app development laboratory works.

## About
This project is a law firm website.

The text content is taken from https://lawflagman.com.ua/

## How to run the project
To run the project execute this command:
`docker-compose -f docker-compose.yml up`

To run migrations:
1. `docker-compose -f docker-compose.yml run web python company/manage.py makemigrations` (сreate new migrations)
2. `docker-compose -f docker-compose.yml run web python company/manage.py migrate`

To create admin account (superuser):
`docker-compose -f docker-compose.yml run web python company/manage.py createsuperuser`

To create (load) "Editors" user group run:
- To dump: `docker-compose -f docker-compose.yml run web python company/manage.py dumpdata auth.group --indent 4 --output datadumps/dumpdata_name.json`
- To load: `docker-compose -f docker-compose.yml run web python company/manage.py loaddata datadumps/dumpdata_name.json`
