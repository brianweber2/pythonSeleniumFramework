pipeline {
    agent { docker { image 'python:3.8.2' } }
    stages {
        stage('Tests') {
            steps {
                sh 'python --version'
            }
        }
    }
}