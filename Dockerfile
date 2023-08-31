FROM python:3.10-alpine

COPY . .
RUN pip install -r requirements.txt

EXPOSE 8080

CMD ["python","main.py"]