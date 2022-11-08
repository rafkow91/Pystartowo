FROM python:3.10
WORKDIR /code
COPY requirements.txt requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
COPY . .
CMD cd pystartowo && ls && gunicorn --bind=0.0.0.0:8000 core.wsgi