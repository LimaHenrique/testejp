#!groovy
pipeline{
    agent any
    stages {
        stage ("Build"){
            steps{
                echo 'Building'
                git 'https://github.com/LimaHenrique/testejp'
                bat '''
                start cmd.exe /c C:Users\\Henrique Lima\\Desktop\\env\\Scripts\\activate
                pip install python-jenkins
                python -m pip install --upgrade pip
                '''
            }
        }
        stage ("Test"){
            steps{
                bat '''
                python -m Pyautomators -f json -o .//testejp.json
                '''
            }
        }
    }
}
