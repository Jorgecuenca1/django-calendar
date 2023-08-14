FROM python:3.8.10
ENV PYTHONUNBUFFERED=1
WORKDIR /code-backend
COPY requirements.txt /code-backend/
RUN pip install -r requirements.txt