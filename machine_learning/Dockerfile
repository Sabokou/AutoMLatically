FROM --platform=linux/amd64 python:3.9

WORKDIR /src

COPY . /src

# install latest update of dependencies
RUN apt-get update 

# install dependencies for the python code
RUN pip install --no-cache-dir -r /src/requirements.txt

CMD [ "python", "/src/run.py" ]