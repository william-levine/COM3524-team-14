FROM python:3.8-slim


WORKDIR /app

COPY . /app


# Install system dependencies including Tk

RUN apt-get update && apt-get install -y \
    gcc \
    tk-dev \
    && rm -rf /var/lib/apt/lists/*

# Install Python packages
RUN pip install --no-cache-dir \
    numpy==1.24.4 \
    Flask \
    eventlet==0.26.1 \
    Flask-SocketIO==5.3.1 \
    gunicorn==20.0.4 \
    matplotlib 

EXPOSE 5000

#Set the environment variable for Flask
ENV FLASK_APP=ACO_Teaching_Tool/antsp/app.py

CMD ["python3", "run_tool.py"]
