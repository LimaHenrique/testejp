#!groovy
pipeline{
    agent any
    stages {
        stage ("Build"){
            steps{
                echo 'Building'
                git 'https://github.com/LimaHenrique/testejp'
            }
        }
        stage ("Test"){
            steps{
                bat '''
                pip install python-jenkins
                python -m pip install --upgrade pip
                pip install virtualenv
                virtualenv env
                env//s//activate
                '''
                bat '''
                cd testejp
                python -m Pyautomators -f json -o .//testejp.json
                '''
              
            }
        }
    }
}
