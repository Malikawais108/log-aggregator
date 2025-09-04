FROM python:3.10-slim
WORKDIR /app
COPY parser/ /app/
RUN pip install prometheus_client
EXPOSE 8000
CMD ["python", "main.py"]

