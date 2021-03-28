pipeline {
    agent { docker { image 'python:3.8.2' } }
    stages {
        stage('Tests') {
            steps {
                withEnv(["HOME=${env.WORKSPACE}"]) {
                  sh "pip install -r requirements.txt --user"
                  sh "python -m pytest --html=tests/report.html tests/ --browser_name chrome"
                }
            }
            post {
                cleanup {
                    cleanWs()
                }
            }
        }
    }
}