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
                /env//s//activate
                '''
                bat '''
                cd testejp
                python -m Pyautomators -f json -o .//testejp.json
                '''
              
            }
        }
    }
}
