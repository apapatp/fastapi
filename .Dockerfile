FROM python:3.6

RUN apt-get update && apt-get install -y \
    vim \
    python3-pip \
    python3-dev \

# Set the working directory as the app dir
# This is needed for tests to be in the right path in the CI
WORKDIR /code/

# Install requirements for python
# COPY requirements.txt /app/requirements.txt
COPY ./requirements.txt /code/requirements.txt

RUN pip install --upgrade pip
RUN pip install -r /code/requirements.txt

COPY ./app /code/app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]