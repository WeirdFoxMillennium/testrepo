FROM python:3

WORKDIR /app

COPY prime_finder.py /app/prime_finder.py

CMD ["python", "/app/prime_finder.py"]