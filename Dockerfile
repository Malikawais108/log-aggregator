FROM python:3.10-slim

WORKDIR /app

# Copy your app code and requirements
COPY parser/ /app/
COPY requirements.txt /app/

# Install all dependencies
RUN pip install -r requirements.txt

EXPOSE 8087

CMD ["python", "main.py"]
