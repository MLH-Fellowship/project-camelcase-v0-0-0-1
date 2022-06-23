# !/bin/bash

#activate source at session level
source venv/bin/activate

#exports the required variables
export FLASK_ENV="development"
export FLASK_APP=run.py

#TODO: Should not push these variables to the cloud
export DB_URL="localhost:5000"
export MYSQL_HOST="localhost"
export MYSQL_USER="myportfolio"
export MYSQL_PASSWORD="mypassword"
export MYSQL_DATABASE="myportfoliodb"

#uses flask CLI to run
flask run --host=0.0.0.0
if [[$? -ne 0 ]]; then
  echo "Unable to run the start Flask Server" >&2
fi