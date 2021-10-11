FROM python:3.9-slim

COPY src/ /app
WORKDIR /app
RUN pip3 install Flask Flask-Cors
EXPOSE 5000
CMD ["python", "app.py"]