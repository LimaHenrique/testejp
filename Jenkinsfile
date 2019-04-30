pipeline {
    
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building..'
                sh 'python --version'
                bat 'pip --version'
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
