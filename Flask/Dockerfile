# fetches Python image based using the amd64 architecture, even if your system has an ARM CPU
FROM --platform=linux/amd64 python:3.9

# setup working directory
WORKDIR /src

# copy folder into working directory
COPY ./src /src

# install latest update of dependencies
RUN apt-get update 

# install dependencies for the python code
RUN pip install --no-cache-dir -r /src/requirements.txt

EXPOSE 8001

CMD ["python", "/src/run.py"]