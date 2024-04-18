FROM python:3.11-alpine

WORKDIR /src

COPY requirements.txt /src/
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python3.11", "-m", "flask", "run", "--host=0.0.0.0"]
