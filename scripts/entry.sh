#! /bin/bash

source venv/bin/activate
while true; do 
  flask deploy
  if [[ "$?" == "0" ]]; then 
    echo "db has been deployed"
    break
  fi 
  echo "deployment failed with code $?, retrying in 5 seconds..."
  sleep 5
done 

flask run --host=0.0.0.0

