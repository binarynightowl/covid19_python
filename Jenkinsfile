pipeline {
  agent any
  stages {
    stage('Init Virtual Envs') {
      steps {
        sh '''PATH=$WORKSPACE/venv/bin:/usr/local/bin:$PATH
if [ ! -d "venv35" ]; then
        virtualenv --python=/usr/local/share/man/man1/python3.5.1 venv35
fi

if [ ! -d "venv36" ]; then
        virtualenv --python=/usr/local/share/man/man1/python3.6.1 venv36
fi

if [ ! -d "venv37" ]; then
        virtualenv --python=/usr/local/share/man/man1/python3.7.1 venv37
fi

if [ ! -d "venv38" ]; then
        virtualenv --python=/usr/local/share/man/man1/python3.8.1 venv38
fi'''
        sh '''. venv35/bin/activate
pip install -r requirements.txt --download-cache=/tmp/$JOB_NAME
. venv35/bin/deactivate

. venv36/bin/activate
pip install -r requirements.txt --download-cache=/tmp/$JOB_NAME
. venv36/bin/deactivate

. venv37/bin/activate
pip install -r requirements.txt --download-cache=/tmp/$JOB_NAME
. venv37/bin/deactivate

. venv38/bin/activate
pip install -r requirements.txt --download-cache=/tmp/$JOB_NAME
. venv38/bin/deactivate'''
      }
    }

  }
}