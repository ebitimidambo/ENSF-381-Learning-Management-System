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
        
        stage('Docker Build & Push') {
            steps {
                echo 'Building Docker image...'
        
                sh 'docker build -t ebitimidambo/web-project:latest .'
        
                echo 'Logging in to Docker Hub and pushing image...'
        
                withCredentials([usernamePassword(
                    credentialsId: 'a43a43ca-fb53-462a-902b-a11cacf2f646',
                    usernameVariable: 'DOCKER_USERNAME',
                    passwordVariable: 'DOCKER_TOKEN'
                )]) {
                    sh '''
                        echo "$DOCKER_TOKEN" | docker login -u "$DOCKER_USERNAME" --password-stdin
                        docker push ebitimidambo/web-project:latest
                        docker logout
                    '''
                }
            }
        }

        stage('Terraform Deploy') {
            steps {
                echo 'Deploying application server with Terraform...'
        
                dir('terraform') {
                    sh 'terraform init'
                    sh 'terraform validate'
                    sh 'terraform plan -out=tfplan'
                    sh 'terraform apply -auto-approve tfplan'
        
                    echo 'Terraform deployment complete.'
                    sh 'terraform output'
                }
            }
        }

        stage('Ansible Configuration') {
            steps {
                echo 'Configuring application server with Ansible...'

                script {
                    env.DEPLOY_SERVER_IP = sh(
                        script: 'cd terraform && terraform output -raw public_ip',
                        returnStdout: true
                    ).trim()
                }

                echo "Terraform deployed server at ${env.DEPLOY_SERVER_IP}"

                sshagent(credentials: ['ensf519-ec2-ssh-key']) {
                    sh '''
                        ansible-playbook \
                            -i "${DEPLOY_SERVER_IP}," \
                            -u ubuntu \
                            --ssh-common-args="-o StrictHostKeyChecking=no" \
                            ansible/playbook.yml
                    '''
                }
            }
        }
    }
}
