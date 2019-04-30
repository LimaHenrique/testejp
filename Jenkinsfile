pipeline {
    
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building..'
                sh 'pip3 --version'
                sh 'pip3 install Pyautomators'
                sh 'pip3 install webautomators'
            }
        }
        stage('Test') {
            steps {
                sh  'python3 -m Pyautomators'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
            }
        }
    }
}
