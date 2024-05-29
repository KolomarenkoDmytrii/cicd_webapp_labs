FROM python
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /app
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
RUN python company/manage.py collectstatic --noinput
CMD tail -f /dev/null
EXPOSE 8000
