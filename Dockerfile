FROM python
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

ENV POSTGRES_DB=${POSTGRES_DB}
ENV POSTGRES_USER=${POSTGRES_USER}
ENV POSTGRES_HOST=${POSTGRES_HOST}
ENV POSTGRES_PASSWORD=${POSTGRES_PASSWORD}

WORKDIR /app
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
RUN python company/manage.py collectstatic --noinput
CMD cd company && gunicorn company.wsgi:application --bind 0.0.0.0:${PORT}
EXPOSE 8000
