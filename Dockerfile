FROM python:3.7

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . mwapp
WORKDIR /mwapp

EXPOSE 8000

ENTRYPOINT ["python", "manage.py"]
CMD ["runserver", "0.0.0.0:8000"]

