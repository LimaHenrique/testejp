pipeline {
    
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building..'
                sh 'source /root/env/bin/activate'
            }
        }
        stage('Test') {
            steps {
                echo 'Test..'
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
