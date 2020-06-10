pipeline {
  agent any
  stages {
    stage('Build') {
      parallel {
        stage('Init Virtual Env (Python 3.5)') {
          steps {
            echo 'Creating Virtual Environment for Python 3.5'
            sh '''#!/bin/sh

PATH=$WORKSPACE/venv/bin:/usr/local/bin:$PATH
if [ ! -d "venv35" ]; then
        virtualenv -p python3.5 venv35
fi'''
            echo 'Populating venv35'
            sh '''#!/bin/sh

. venv35/bin/activate
pip install -r requirements.txt
pip install pytest
pip install pytest-cov
deactivate'''
            echo 'venv35 has been successfully created!'
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