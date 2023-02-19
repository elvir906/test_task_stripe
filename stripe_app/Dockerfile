FROM python:3
WORKDIR /app
COPY requirements.txt .
RUN pip3 install --no-cache-dir -r /app/requirements.txt
COPY stripe_app .
CMD ["gunicorn", "bot.wsgi:application", "--bind", "0:8000" ]