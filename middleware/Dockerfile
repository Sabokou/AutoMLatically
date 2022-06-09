# pull official base image
FROM --platform=linux/amd64 node:18

WORKDIR /app
# mount the files from the current folder to the container working directory
VOLUME .:/app

# # copy code to working dir
COPY . /app
# update to newest npm version
RUN npm install npm --silent
# install dependencies for the middleware server
RUN npm install --save multer file upload nodemon cors express --silent

# open port 8000 for connections
EXPOSE 8000

# start app
CMD ["npx", "nodemon", "/app/server.js"]