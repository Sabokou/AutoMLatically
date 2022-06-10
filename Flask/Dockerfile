# fetches Python image based using the amd64 architecture, even if your system has an ARM CPU
FROM --platform=linux/amd64 python:3.9

# setup working directory
WORKDIR /app

# copy folder into working directory
COPY ./Flask/src /app
COPY ./check_volume_mounted.bash /app

# install latest update of dependencies
RUN apt-get update 

# install dependencies for the python code
RUN pip install --no-cache-dir -r /app/requirements.txt

EXPOSE 8001

# check if the volume is mounted at /volume and use the files in it.
# otherwise use the copied files in /app 
COPY ./check_volume_mounted.bash /app
CMD . /app/check_volume_mounted.bash && python ${BASE_DIR}/run.py
# CMD ["python", "/src/run.py"]