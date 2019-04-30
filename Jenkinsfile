pipeline {
    
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building..'
                sh 'python3 pip install Pyautomators'
                sh 'python3 pip install webautomators'
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
