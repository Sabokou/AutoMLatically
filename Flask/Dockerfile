# fetches Python image based on Slim
FROM python:3.9-slim

# setup working directory
WORKDIR /src

# copy folder into working directory
COPY ./Flask /src

# install requirements
COPY /Flask/requirements.txt requirements.txt
RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["python", "/src/run.py"]