# pull official base image
FROM --platform=linux/amd64 node:18

WORKDIR /app

# # copy code to working dir
COPY ./middleware /app
# update to newest npm version
RUN npm install npm --silent
# install dependencies for the middleware server
RUN npm install --silent

# add `/app/node_modules/.bin` to $PATH, so that the installed binaries are recognized by node 
ENV PATH /app/node_modules/.bin:$PATH

# open port 8000 for connections
EXPOSE 8000


# check if the volume is mounted at /volume and use the files in it.
# otherwise use the copied files in /app 
COPY ./check_volume_mounted.bash /app
CMD . /app/check_volume_mounted.bash && cd ${BASE_DIR} && npx nodemon server.js
# for Apple Silicon users: add the following in the upper CMD before the npm start:
# && npm install --silent --save

# start app
#CMD ["npx", "nodemon", "/app/server.js"]