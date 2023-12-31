#!/usr/bin/env bash

echo 'check if envinronment already exists'
if test -d env/; then
  echo "Directory exists."
  echo 'activating the virtual environment'
  source env/bin/activate

  echo 'installing dependencies'
  pip install -r requirements.txt

    echo 'done, you may run the app by typing "python3 MacPom"'
else
echo 'creating a Python virtual environment'

python3 -m venv env --prompt=MacPom

echo 'activating the virtual environment'
source env/bin/activate

echo 'installing dependencies'
pip install -r requirements.txt

echo 'done, you may run the app by typing "python3 MacPom"'

fi


