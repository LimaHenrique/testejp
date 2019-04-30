pipeline {
    
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building..'
                sh '''
                echo $PATH
                yum install python-pip                
                pip install Pyautomators
                '''
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
