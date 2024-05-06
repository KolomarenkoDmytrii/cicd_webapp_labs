# cicd_webapp_labs
CI/CD web-app development laboratory works.

# Run Docker image
1. `docker build -t cicd-webapp .`
2. `docker run -dp 127.0.0.1:8000:8000 cicd-webapp`

...or to run with database (PostgreSQL):
`docker compose -f docker-compose.yml up`

To run migrations:
`docker-compose run web python company/manage.py migrate`

To create admin account (superuser):
`docker-compose run web python company/manage.py createsuperuser`
