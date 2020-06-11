pipeline {
  agent any
  stages {
    stage('Build') {
      parallel {
        stage('Init Virtual Env (Python 3.5)') {
          steps {
            timestamps() {
              echo 'Creating Virtual Environment for Python 3.5'
            }

            sh '''#!/bin/sh

PATH=$WORKSPACE/venv/bin:/usr/local/bin:$PATH
if [ ! -d "venv35" ]; then
        virtualenv -p python3.5 venv35
fi'''
            timestamps() {
              echo 'Populating venv35'
            }

            sh '''#!/bin/sh

. venv35/bin/activate
pip install -r requirements.txt
pip install pytest
pip install pytest-cov
deactivate'''
            timestamps() {
              echo 'venv35 has been successfully created!'
            }

          }
        }

        stage('Init Virtual Env (Python 3.6)') {
          steps {
            timestamps() {
              echo 'Creating Virtual Environment for Python 3.6'
            }

            sh '''#!/bin/sh

PATH=$WORKSPACE/venv/bin:/usr/local/bin:$PATH
if [ ! -d "venv36" ]; then
        virtualenv -p python3.6 venv36
fi'''
            timestamps() {
              echo 'Populating venv36'
            }

            sh '''#!/bin/sh

. venv36/bin/activate
pip install -r requirements.txt
pip install pytest
pip install pytest-cov
deactivate'''
            timestamps() {
              echo 'venv36 has been successfully created!'
            }

          }
        }

        stage('Init Virtual Env (Python 3.7)') {
          steps {
            timestamps() {
              echo 'Creating Virtual Environment for Python 3.7'
            }

            sh '''#!/bin/sh

PATH=$WORKSPACE/venv/bin:/usr/local/bin:$PATH
if [ ! -d "venv37" ]; then
        virtualenv -p python3.7 venv37
fi'''
            timestamps() {
              echo 'Populating venv37'
            }

            sh '''#!/bin/sh

. venv37/bin/activate
pip install -r requirements.txt
pip install pytest
pip install pytest-cov
deactivate'''
            timestamps() {
              echo 'venv37 has been successfully created!'
            }

          }
        }

        stage('Init Virtual Env (Python 3.8)') {
          steps {
            timestamps() {
              echo 'Creating Virtual Environment for Python 3.8'
            }

            sh '''#!/bin/sh

PATH=$WORKSPACE/venv/bin:/usr/local/bin:$PATH
if [ ! -d "venv38" ]; then
        virtualenv -p python3.8 venv38
fi'''
            timestamps() {
              echo 'Populating venv38'
            }

            sh '''#!/bin/sh

. venv38/bin/activate
pip install -r requirements.txt
pip install pytest
pip install pytest-cov
pip install flake8
deactivate'''
            timestamps() {
              echo 'venv38 has been successfully created!'
            }

          }
        }

        stage('Init Virtual Env (PyPy3)') {
          steps {
            timestamps() {
              echo 'Creating Virtual Environment for PyPy3'
            }

            sh '''#!/bin/sh

PATH=$WORKSPACE/venv/bin:/usr/local/bin:$PATH
if [ ! -d "venv_pypy3" ]; then
        virtualenv -p pypy3 venv_pypy3
fi'''
            timestamps() {
              echo 'Pupulating venv_pypy3'
            }

            sh '''#!/bin/sh

. venv_pypy3/bin/activate
pip install -r requirements.txt
pip install pytest
pip install pytest-cov
deactivate'''
            timestamps() {
              echo 'venv_pypy3 has been successfully created!'
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

pytest'''
          }
        }

        stage('Python 3.6') {
          steps {
            sh '''#!/bin/sh

. venv36/bin/activate

pytest'''
          }
        }

        stage('Python 3.7') {
          steps {
            sh '''#!/bin/sh

. venv37/bin/activate

pytest'''
          }
        }

        stage('Python 3.8') {
          steps {
            sh '''#!/bin/sh

. venv38/bin/activate

pytest'''
          }
        }

        stage('PyPy3') {
          steps {
            sh '''#!/bin/sh

. venv_pypy3/bin/activate

pytest'''
          }
        }

      }
    }

    stage('Code Check') {
      parallel {
        stage('Message') {
          steps {
            timestamps() {
              echo 'Build passing! Now linting and checking code!'
            }

          }
        }

        stage('PyLint') {
          steps {
            sh '''. venv38/bin/activate
pylint --generate-rcfile
pylint -j 0 -r n covid19_data'''
          }
        }

      }
    }

    stage('Clean Up') {
      steps {
        timestamps() {
          cleanWs(cleanWhenSuccess: true, skipWhenFailed: true)
        }

      }
    }

  }
}