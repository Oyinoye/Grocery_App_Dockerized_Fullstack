# pull official base image
FROM node:13.12.0-alpine

# set working directory
WORKDIR /app/frontend

# add `/app/node_modules/.bin` to $PATH
ENV PATH /app/frontend/node_modules/.bin:$PATH

# install app dependencies
COPY package.json ./
COPY yarn.lock ./

RUN CI=true

RUN yarn install --ignore-engines --silent
RUN yarn global add react-scripts@3.4.1

# add app
COPY . ./

# start app
CMD ["yarn", "start"]