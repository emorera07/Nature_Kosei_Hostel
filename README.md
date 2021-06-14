Nature_Kosei_Hostel
Django, Python3, Ubuntu 20.04.2

Web page for appointment scheduling Html proyect to create a web page to control appointment scheduling for the Nature Kosei Hostel
Requierements

-Docker version 20.10.2 or above, build in 20.10.2-0ubuntu1~20.04.2
How to Run

Clone the repository:

git clone git@github.com:emorera07/Nature_Kosei_Hostel.git

Into the root folder:
Build the Docker

sudo docker build --tag djangoweb:latest .
Run the docker with the port 8000 exposed and start bash:

sudo docker run -p 8000:8000 -ti djangoweb:latest bash

now the shell in the docker is open. Then run:

cd home/Nature_Kosei_Hostel/

python3 manage.py makemigrations

python3 manage.py migrate

python3 manage.py runserver 0.0.0.0:8000
The server is up and and can be accessed through the URL shown as a link in the console
brandon.esquivel@ucr.ac.cr,
emmanuel.morera@ucr.ac.cr
