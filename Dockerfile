FROM python:3.8

# copy working dir
WORKDIR /home
ADD . /home

# define args
ARG api_port=8080
ARG auth_token=sometoken

# export env vars
ENV API_PORT=$api_port
ENV AUTH_TOKEN=$auth_token

# install dependencies
RUN pip install --no-cache-dir -r req.txt

ENTRYPOINT gunicorn --bind 0.0.0.0:$API_PORT --workers 2 simpletokenizerapi:app
EXPOSE $api_port