############
#### You might have to grant permissions to allow this script to run
#### This script must be called from the root directory 
############

#activate source at session level
source venv/bin/activate

#exports the required variables
# export FLASK_ENV="development"
export FLASK_APP=run.py

#uses flask CLI to run
# flask run

flask run --host=0.0.0.0
# flask run
if [[$? -ne 0 ]]; then
  echo "Unable to run the start Flask Server" >&2
fi