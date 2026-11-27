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
                echo 'Cleaning previous build artifacts...'
                sh 'rm -rf build'
                
                echo 'Installing frontend dependencies...'
                sh 'npm ci'

                echo 'Building React application...'
                sh 'CI=false npm run build'
            }
        }
        stage('Automated Testing') {
            steps {
                echo 'Running Selenium automated tests...'
        
                sh '''
                    python3 -m venv .venv
                    .venv/bin/pip install flask flask-cors selenium
        
                    .venv/bin/flask --app Backend/app.py run --host=127.0.0.1 --port=5000 > backend.log 2>&1 &
                    BACKEND_PID=$!
        
                    CI=false npm start > frontend.log 2>&1 &
                    FRONTEND_PID=$!
        
                    trap 'kill $BACKEND_PID $FRONTEND_PID 2>/dev/null || true' EXIT
        
                    sleep 10
        
                    .venv/bin/python selenium_tests/*.py
                '''
            }
        }
    }
}
