FROM python:3.9.17

# Expose ports
EXPOSE 80 8000

# Disable debian warnings!
ENV DEBIAN_FRONTEND noninteractive

RUN apt update
RUN apt -y install pkg-config
RUN apt -y install software-properties-common
RUN apt -y install postgresql postgresql-contrib

# Set the default directory where CMD will execute
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app
ADD pyproject.toml /usr/src/app/
ADD poetry.lock /usr/src/app/

RUN pip install --upgrade pip
RUN pip install poetry
RUN poetry install --no-root
ADD . /usr/src/app/
