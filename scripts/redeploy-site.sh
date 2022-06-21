cd /root/personal-portfolio
if [[ $? -ne 0 ]]
  then 
    echo 'Personal Portfolio not found!' >&2
    exit 1
fi

# tmux new -s project_inst
git fetch && git reset origin/main --hard
if [[ $? -ne 0 ]]; then
  echo "Warning: Unable to fetch updates" >&2
fi

tmux new-session -d -s flask_instance
tmux send-keys -t flask_instance "./scripts/launch.zsh" Enter

# tmux attach