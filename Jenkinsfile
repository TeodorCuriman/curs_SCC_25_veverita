pipeline {
  agent any
  stages {
    stage('Checkout') {
      steps { checkout scm }
    }
    stage('Install') {
      steps { sh 'pip install -r requirements.txt' }
    }
    stage('Test') {
      steps { sh 'pytest --maxfail=1 --disable-warnings -q' }
    }
    stage('Build Docker image'){
       steps {
sh 'docker build -t veverita_app .'
	}
    }
  }
  post {
    always {
         echo 'Pipeline finished (success or failure)'
    }
  }
}
