# Build me with
# docker build --tag djangoweb:latest .
# docker run -p 80:8000 -ti <app> bash

# Define base OS
FROM ubuntu:20.04

ENV TZ=America/Costa_Rica
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime \
    && echo $TZ > /etc/timezone

# Info Labels
LABEL mantainer="brandon.esquivel@ucr.ac.cr"
LABEL version="1.0"
LABEL description="Custom docker image for a Django Web app"

# Choose user root
USER root

# Install dependencies and requirements
RUN apt update \
    && apt --yes --no-install-recommends install \
        build-essential cmake libgtest-dev git \
        add-apt-repository ppa:deadsnakes/ppa \
        software-properties-common sqlite3 libsqlite3-dev \ 
        python3.9 python3 python3-venv python3-pip \
        
RUN python3.9 -m pip install Django
RUN python3 -m pip install Django
RUN export PATH=/home/bran/.local/bin:$PATH
          
# Create project folder
RUN mkdir -p /home/Nature_Kosei_Hostel

# Copy local files to container
COPY static /home/Nature_Kosei_Hostel/static
COPY Nature_Kosei_Hostel /home/Nature_Kosei_Hostel/Nature_Kosei_Hostel
COPY appointments /home/Nature_Kosei_Hostel/appointments
COPY static /home/Nature_Kosei_Hostel/static
COPY users home/Nature_Kosei_Hostel/users
COPY manage.py home/Nature_Kosei_Hostel/manage.py
COPY README.md /home/Nature_Kosei_Hostel/README.md

# executable
EXPOSE 8000
RUN cd /home/Nature_Kosei_Hostel
RUN python3.9 manage.py runserver 8000
