FROM python:latest
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
CMD ["python", "company/manage.py", "runserver", "0.0.0.0:8000"]
EXPOSE 8000
