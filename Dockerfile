FROM python
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /app
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
RUN python company/manage.py collectstatic --noinput
#CMD ["python", "company/manage.py", "runserver", "0.0.0.0:8000"]
#CMD ["gunicorn", "hello_django.wsgi:application", "--bind 0.0.0.0:8000"]
CMD tail -f /dev/null
EXPOSE 8000
