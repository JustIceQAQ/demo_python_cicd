pipeline {
  agent any
  stages {
    stage('version') {
      steps {
        bat 'python3 --version'
      }
    }
    stage('runserver') {
      steps {
        bat 'python -m uvicorn main:app --reload --port 8787 --host 0.0.0.0'
      }
    }
  }
}