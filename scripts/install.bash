echo "[HELP]: pip install $1 (\$1) && pip freeze | grep "$1 \(\$1\)" >> $2 (\$2)"
read -p "Are you Sure? [Y/n] " user_input

case $user_input in 
  [Yy]* )
    pip install $1 && pip freeze | grep "$1" >> $2
    break;
esac