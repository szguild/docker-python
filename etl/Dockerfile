FROM python:3.8-slim

WORKDIR /etl

# pip freeze > requirements.txt
COPY requirements.txt ./

RUN python -m pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python3", "main.py" ]