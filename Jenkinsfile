pipeline {
    
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building..'
                bat './Users/Henrique Lima/Desktop/env/Scripts/activate'
            }
        }
        stage('Test') {
            steps {
                echo 'Test..'
                bat  'python -m Pyautomators'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
            }
        }
    }
}
