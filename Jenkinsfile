pipeline {
    
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building..'
                sh 'pip3.6 --version'
                sh 'pip3.6 install Pyautomators'
                sh 'pip3.6 install webautomators'
            }
        }
        stage('Test') {
            steps {
                sh  'python3.6 -m Pyautomators'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
            }
        }
    }
}
