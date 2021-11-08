FROM python:3.10-alpine
WORKDIR /app
COPY . . 
RUN pip install flask
ENTRYPOINT ["python"]
EXPOSE 5000
CMD ["svc-b.py"]
