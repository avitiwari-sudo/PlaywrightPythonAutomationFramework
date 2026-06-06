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
                C:\\Users\\avika\\AppData\\Local\\Programs\\Python\\Python314\\python.exe --version
                """
            }
        }

        stage('Install dependencies') {
            steps {
                bat """
                 C:\\Users\\avika\\AppData\\Local\\Programs\\Python\\Python314\\python.exe -m pip install -r requirements.txt
                 C:\\Users\\avika\\AppData\\Local\\Programs\\Python\\Python314\\python.exe -m pip install allure-pytest pytest-xdist pytest-rerunfailures
                 C:\\Users\\avika\\AppData\\Local\\Programs\\Python\\Python314\\python.exe -m playwright install
                """
            }
        }

        stage('Run tests') {
            steps {
                bat """
                 C:\\Users\\avika\\AppData\\Local\\Programs\\Python\\Python314\\python.exe -m pytest --alluredir=allure-results
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
