# Build me with
# sudo docker build --tag djangoweb:latest .
# Run me with
# sudo docker run -p 8000:8000 -ti djangoweb:latest bash
# Then, the docker is up, run the server:
# >> cd home/Nature_Kosei_Hostel/
# >> python3 manage.py migrate
# >> python3 manage.py runserver 8000 

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

# Install dependencies and requirements, #firewalld
RUN apt update && apt --yes --no-install-recommends install build-essential cmake libgtest-dev git 
RUN apt -y install software-properties-common sqlite3 libsqlite3-dev python3.9 python3 python3-venv python3-pip
RUN add-apt-repository ppa:deadsnakes/ppa        
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

# TCP ports
EXPOSE 8080
EXPOSE 8000
EXPOSE 80
EXPOSE 443

# exe> where?
#RUN cd /home/Nature_Kosei_Hostel
#CMD python3 manage.py makemigrations
#CMD python3 manage.py migrate
#CMD python3 manage.py runserver 80
