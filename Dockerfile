FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt
RUN pip install psycopg2-binary

COPY . .

CMD ["python", "manage.py", "runserver"]