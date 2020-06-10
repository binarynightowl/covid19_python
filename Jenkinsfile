pipeline {
  agent any
  stages {
    stage('Init Virtual Envs') {
      steps {
        sh '''#!/bin/sh

PATH=$WORKSPACE/venv/bin:/usr/local/bin:$PATH
if [ ! -d "venv35" ]; then
        virtualenv -p python3.5 venv35
fi

if [ ! -d "venv36" ]; then
        virtualenv -p python3.6 venv36
fi

if [ ! -d "venv37" ]; then
        virtualenv -p python3.7 venv37
fi

if [ ! -d "venv38" ]; then
        virtualenv -p python3.8 venv38
fi'''
        sh '''#!/bin/sh

. venv35/bin/activate
pip install -r requirements.txt
deactivate

. venv36/bin/activate
pip install -r requirements.txt
deactivate

. venv37/bin/activate
pip install -r requirements.txt
deactivate

. venv38/bin/activate
pip install -r requirements.txt
deactivate'''
      }
    }

  }
}