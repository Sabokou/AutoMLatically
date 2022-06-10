# pull official base image
FROM --platform=linux/amd64 node:18

WORKDIR /app

# # copy code to working dir
COPY ./frontend /app
RUN apt-get update
# update npm version
#RUN npm install npm --silent
# install dependencies that are not automatically installed by "npm install"
#RUN npm install react-scripts bootstrap react-bootstrap axios --silent --save
# install app dependencies
RUN npm install --silent --save

# add `/app/node_modules/.bin` to $PATH, so that the installed binaries are recognized by node 
ENV PATH $PATH:/app/node_modules/.bin:/volume/node_modules/.bin

EXPOSE 3000

# check if the volume is mounted at /volume and use the files in it.
# otherwise use the copied files in /app 
COPY ./check_volume_mounted.bash /app
CMD . /app/check_volume_mounted.bash && cd ${BASE_DIR} && npm start
# for Apple Silicon users: add the following in the upper CMD before the npm start:
# && npm install --silent --save

# start app
#CMD ls && npm start