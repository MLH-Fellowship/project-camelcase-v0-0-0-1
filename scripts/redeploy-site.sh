#!/bin/bash
tmux kill-session
cd project-camelcase-v0-0-0-1
git fetch && git reset origin/main --hard
source python3-virtualenv/bin/activate
pip install -r requirements.txt
tmux new -ds portfolio 'python -m venv python3-virtualenv;
source python3-virtualenv/bin/activate;
pip install -r requirements.txt;
flask run --host=0.0.0.0;
exec $SHELL'

