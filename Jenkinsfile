pipeline {
    
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building..'
                sh 'chmod 777 driver/chromedriver.exe'
            }
        }
        stage('Test') {
            steps {
                echo 'Test..'
                sh  'python -m unittest discover --pattern=test.py'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
            }
        }
    }
}
