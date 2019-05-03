#!groovy
pipeline{
    agent any
    stages {
        stage ("Build"){
            steps{
                echo 'Building'
                git 'https://github.com/LimaHenrique/testejp'
                bat '''
                start cmd.exe /c C:\\Program Files (x86)\\Jenkins\\workspace\\DesafioJP\\env\\Scripts\\activate
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
