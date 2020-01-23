FROM python:3-alpine
WORKDIR /app
COPY requirements.txt /app
RUN pip install --no-cache-dir -r requirements.txt
COPY . /app
EXPOSE 80
CMD python3 api.py
ENV PYTHONUNBUFFERED=1
