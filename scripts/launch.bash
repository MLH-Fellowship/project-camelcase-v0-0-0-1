# !/bin/bash

#activate source at session level
source venv/bin/activate

#exports the required variables
export FLASK_ENV="development"
export FLASK_APP=run.py

#uses flask CLI to run
flask run --host=0.0.0.0
if [[ $? -ne 0 ]]; then
  echo "Unable to start Flask Server <Make sure Flask has been installed>" >&2
fi