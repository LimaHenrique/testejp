pipeline {
    
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building..'
                sh 'python --version'
                sh 'apk install python-pip'
                sh 'pip install Pyautomators'
                sh 'pip install webautomators'
            }
        }
        stage('Test') {
            steps {
                sh  'python -m Pyautomators'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
            }
        }
    }
}
