pipeline {
    agent any
    stages {
        stage('Build Docker Image') {
            steps {
                script {
                    sh 'docker build -t veverita-app .'
                }
            }
        }
        stage('Run Container') {
            steps {
                script {
                    sh 'docker run --rm veverita-app'
                }
            }
        }
    }
}
