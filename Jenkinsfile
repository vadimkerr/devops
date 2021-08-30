pipeline {
    agent {
        docker {
            image 'python:3.9-alpine'
            args '-u root:root'
        }
    }

    stages {
        stage('checkout') {
            steps {
                checkout scm
            }
        }

        stage('install dependencies') {
            steps {
                sh 'apk --no-cache add build-base=0.5-r2 && pip --no-cache-dir install pipenv==2021.5.29'
                sh 'cd app_python && pipenv install --system --dev'
            }
        }

        stage('lint') {
            steps {
                sh 'pre-commit run --all-files'
            }
        }

        stage('test') {
            steps {
                sh 'pytest app_python/tests'
            }
        }
    }
}
