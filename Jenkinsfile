#!groovy
pipeline{
    agent any
    stages {
        stage ("Build"){
            steps{
                echo 'Building'
                git 'https://github.com/LimaHenrique/testejp'
                bat label: '', script: '''
                pip install python-jenkins
                python -m pip install --upgrade pip
                pip install virtualenv
                virtualenv env
                env//Scripts//activate
                '''
            }
        }
        stage ("Test"){
            steps{
               bat label: '', script: '\'python -m Pyautomators -f json -o .testejp.json\''
            }
        }
    }
}
