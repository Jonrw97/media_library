#! /bin/sh

#tell flask which folder to access
export FLASK_APP=plex

#to run in development mode
export FLASK_ENV=development

#to initilize database
flask init-db

#run app
flask run