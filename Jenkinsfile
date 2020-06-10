pipeline {
  agent any
  stages {
    stage('Build') {
      parallel {
        stage('Init Virtual Envs') {
          steps {
            echo 'Creating Virtual Environments'
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
            echo 'Populating Virtual Environments'
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
            echo 'Virtual Environments have been created!'
          }
        }

        stage('Timestamp') {
          steps {
            timestamps() {
              echo 'Build Started at'
            }

          }
        }

      }
    }

    stage('Tests') {
      parallel {
        stage('Python 3.5') {
          steps {
            sh '''#!/bin/sh

. venv35/bin/activate

pip install pytest
pip install pytest-cov

pytest'''
          }
        }

        stage('Python 3.6') {
          steps {
            sh '''#!/bin/sh

. venv36/bin/activate

pip install pytest
pip install pytest-cov

pytest'''
          }
        }

        stage('Python 3.7') {
          steps {
            sh '''#!/bin/sh

. venv37/bin/activate

pip install pytest
pip install pytest-cov

pytest'''
          }
        }

        stage('Python 3.8') {
          steps {
            sh '''#!/bin/sh

. venv38/bin/activate

pip install pytest
pip install pytest-cov

pytest'''
          }
        }

      }
    }

    stage('Clean Up') {
      parallel {
        stage('Clean Workspace') {
          steps {
            cleanWs(cleanWhenSuccess: true, skipWhenFailed: true)
          }
        }

        stage('Timestamp') {
          steps {
            timestamps() {
              echo 'Complete!'
            }

          }
        }

      }
    }

  }
}