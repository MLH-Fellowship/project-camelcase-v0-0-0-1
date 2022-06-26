# !/bin/bash
# cd /root/personal-portfolio
# if [[ $? -ne 0 ]]
#   then 
#     echo 'Personal Portfolio not found!' >&2
#     exit 1
# fi


if [[ \ $*\  == *\ --pull-update\ * ]] || [[ \ $*\  == *\ -p\ * ]]; then
  echo "Pulling Update"
  # fetch new updates
  git fetch && git reset origin/main --hard
  if [[ $? -ne 0 ]]; then
    echo "Fatal: Unable to fetch updates" >&2
    exit 1
  fi
fi

if [[ \ $*\  == *\ --update-env-prod\ * ]]; then
  echo "Updating env with prod"
  source ./venv/bin/activate
  pip install -r requirements/prod.txt
  if [[ $? -ne 0 ]]; then
    echo "Warning: Unable to update virtual environment" >&2
  fi
fi


if [[ \ $*\  == *\ --update-env-dev\ * ]]; then
  echo "Updating env with dev"
  source ./venv/bin/activate
  pip install -r requirements/dev.txt
  if [[ $? -ne 0 ]]; then
    echo "Warning: Unable to update virtual environment" >&2
  fi
fi


if [[ \ $*\  == *\ --update-env\ * ]]; then
  echo "[UPDATE-ENV: HELP] provide which config to update env with. --update-env-dev for development config, --update-env-prod for production env" >&2
fi


#TODO: update to check if tmux session 'flask_instance' exists if-so, end it
if [[ \ $*\  == *\ --with-tmux\ * ]]; then
  echo "starting server with tmux"
  tmux new-session -d -s flask_instance
  tmux send-keys -t flask_instance "./scripts/launch.bash" Enter
else
  echo "WARMING: Tmux not set, server starting on the foreground. Use '--with-tmux' to start server on the background with tmux"
  "./scripts/launch.bash"
fi

# tmux attach