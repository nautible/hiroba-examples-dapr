FROM python:3.9-slim

WORKDIR /app
COPY . .
RUN pip3 install Flask Flask-Cors
EXPOSE 5000
CMD ["python", "app.py"]