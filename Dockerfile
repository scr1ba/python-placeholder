FROM python:3.9-alpine
WORKDIR /app
COPY . /app
RUN pip install flask
CMD ["python", "app.py"]
