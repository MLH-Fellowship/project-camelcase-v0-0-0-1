############
#### You might have to grant permissions to allow this script to run
#### This script must be called from the root directory 
############

#activate source at session level
source ./python3-virtualenv/bin/activate

#exports the required variables
export FLASK_ENV="development"
export FLASK_APP=run.py

#uses flask CLI to run
flask run --host=0.0.0.0