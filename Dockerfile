FROM python:3.10-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY app.py .

ARG APP_VERSION
ENV APP_VERSION=${APP_VERSION}
LABEL version=${APP_VERSIPN}

EXPOSE 5000
CMD ["python", "app.py"]

