pipeline {
    
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building..'
                sh 'python --version'
                sh 'sudo apt-get install python-pip'
                sh 'sudo pip install Pyautomators'
                sh 'sudo pip install webautomators'
            }
        }
        stage('Test') {
            steps {
                sh  'sudo python -m Pyautomators'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
            }
        }
    }
}
