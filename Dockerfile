
# the below line downloads the python image
FROM python:3.12-slim-buster 

# the below line installs aswcli [cli is a terminal] to deploy on AWS
RUN apt update -y && install awscli -y
WORKDIR /app


# the below line copies all the source[src] code
COPY . /app
RUN pip install -r requirements.txt
#  the above line installs all the requirements that are required for the project

# the below line runs app.py which is my end point
CMD ["python3", "app.py"]