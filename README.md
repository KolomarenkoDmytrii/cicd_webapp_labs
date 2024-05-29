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

## Mini-guide: How to deploy dockerized app to Heroku
1. Login to Heroku: `heroku login`
2. Login to Heroku Container Registry: `heroku container:login`
3. Build and push an image: `heroku container:push web --app knu-cicd-web-app-lab` 
   (Dockerfile with CMD to run server must be available)
4. Release the pushed image: `heroku container:release web --app knu-cicd-web-app-lab`
