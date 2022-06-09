# pull official base image
FROM --platform=linux/amd64 node:18

WORKDIR /app
# mount the files from the current folder to the container working directory
VOLUME .:/app

# add `/app/node_modules/.bin` to $PATH, so that the installed binaries are recognized by node 
ENV PATH /app/node_modules/.bin:$PATH

# # copy code to working dir
COPY . /app
# update npm version
RUN npm install npm
# install dependencies that are not automatically installed by "npm install"
RUN npm install react-scripts bootstrap react-bootstrap axios --silent
# install app dependencies
RUN npm install --silent

EXPOSE 3000

# start app
CMD ["npm", "start"]