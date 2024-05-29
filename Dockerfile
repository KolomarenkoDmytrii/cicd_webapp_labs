FROM python
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /app
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
RUN python company/manage.py collectstatic --noinput
CMD bash -c "cd company && python manage.py test && gunicorn company.wsgi:application --bind 0.0.0.0:8000"
EXPOSE 8000
