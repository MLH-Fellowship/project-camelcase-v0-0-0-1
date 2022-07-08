# !/bin/bash
# cd /root/personal-portfolio
# if [[ $? -ne 0 ]]
#   then 
#     echo 'Personal Portfolio not found!' >&2
#     exit 1
# fi
#./scripts/redeploy-site.bash --with-tmux --pull-update --update-env-prod 
#./scripts/redeploy-site.bash --with-tmux --update-env-prod 

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

if [[ \ $*\  == *\ --deploy-db\ * ]]; then
  export DB_URL="localhost:5000"
  export MYSQL_HOST="localhost"
  export MYSQL_USER="myportfolio"
  export MYSQL_PASSWORD="mypassword"
  export MYSQL_DATABASE="myportfoliodb"
  flask deploy
fi

#TODO: update to check if tmux session 'flask_instance' exists if-so, end it
if [[ \ $*\  == *\ --with-tmux\ * ]]; then
  echo "starting server with tmux"

  tmux ls | grep "flask_instance" && tmux kill-session -t flask_instance

  tmux new-session -d -s flask_instance
  tmux send-keys -t flask_instance "./scripts/launch.bash" Enter
fi

if [[ \ $*\  == *\ --with-service\ * ]]; then
  # systemctl start myportfolio # - for reference
  # systemctl enable myportfolio # - for reference
  echo "Starting server with system service"
  systemctl daemon-reload
  systemctl restart myportfolio
  if [[ $? -ne 0 ]]; then
    echo "Unable to start service, ensure service has been defined" >&2
    exit 1
  fi
  sleep 1s
  systemctl status myportfolio
fi

if [[ \ $*\  == *\ --dev-mode\ * ]]; then
  echo "WARMING: starting app in dev mode"
  if [[ \ $*\  == *\ --global\ * ]]; then
    ./scripts/launch.bash
  else 
    ./scripts/launch.bash --dev
  fi
fi

if [[ \ $*\  == *\ --with-docker\ * ]]; then
  docker compose -f docker-compose.yml down
  if [[ "$?" != "0" ]]; then 
    echo "WARNING: unable to bring down container"
  fi 

  docker compose -f docker-compose.yml up -d --build
  if [[ "$?" != "0" ]]; then 
    echo "WARNING: unable to build container"
  fi
fi


if [[ \ $*\  == *\ --help\ * ]]; then
  printf "Here are all of the options available\
        \n\t--pull-update      => Gets the latest update from github\
        \n\t--update-env-prod  => Updates the virtual environment using production dependencies\
        \n\t--update-env-dev   => Udpates the virtual environment using development dependencies\
        \n\t--with-tmux        => Starts the application using a tmux session deattached\
        \n\t--with-service     => Starts the application using a service\
        \n\t--dev-mode         => Starts the application in dev mode without tmux or a service\
        \n\t--with-docker      => Starts the application with docker by recomposing images\
        \n\t--help             => Shows this menu\
        "
else 
  echo "\nExiting deploy script. Use --help for more"
fi

# tmux attach