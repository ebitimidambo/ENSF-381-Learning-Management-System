pipeline {
    agent any

    stages {
        stage('Verify Checkout') {
            steps {
                echo 'GitHub repository successfully checked out by Jenkins.'
                sh 'pwd'
                sh 'ls -la'
            }
        }

        stage('Build') {
            steps {
                echo 'Installing frontend dependencies...'
                sh 'npm install'

                echo 'Building React application...'
                sh 'CI=false npm run build'
            }
        }
    }
}
