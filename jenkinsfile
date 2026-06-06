pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Set up Python') {
            steps {
                bat """
                python --version
                """
            }
        }

        stage('Install dependencies') {
            steps {
                bat """
                pip install -r requirements.txt
                pip install allure-pytest pytest-xdist pytest-rerunfailures
                playwright install
                """
            }
        }

        stage('Run tests') {
            steps {
                bat """
                pytest --alluredir=allure-results
                """
            }
        }

        

        stage('Publish Allure report') {
            steps {
                allure results: [[path: 'allure-results']]
            }
        }
    }

    post {
        always {
            archiveArtifacts artifacts: 'logs/**/*.log', fingerprint: true, allowEmptyArchive: true
            archiveArtifacts artifacts: 'allure-results/**', fingerprint: true, allowEmptyArchive: true
        }
    }
}
