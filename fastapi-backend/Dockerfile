FROM python:3.13

WORKDIR /usr/src/app/backend

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8081

CMD ["sh","-c","sleep 5 && fastapi run main.py --port 8081"]
