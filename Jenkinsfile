pipeline {
    // agent { docker { image 'python:3.5.1' } }
    agent { dockerfile true }
    stages {
        stage('build') {
            steps {
                sh 'python --version'
            }
        }

        stage('test') {
      		steps {
        		sh 'python test.py'
      }   
    }
    }
}