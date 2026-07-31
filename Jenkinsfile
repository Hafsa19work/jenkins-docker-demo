pipeline {
    agent any

    environment {
        IMAGE = "hafsaaqeel/myapp"
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/Hafsa19work/jenkins-docker-demo.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t $IMAGE:$BUILD_NUMBER -t $IMAGE:latest .'
            }
        }

        stage('Push to Docker Hub') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'dockerhub-creds',
                                                  usernameVariable: 'USER',
                                                  passwordVariable: 'TOKEN')]) {
                    sh '''
                        echo "$TOKEN" | docker login -u "$USER" --password-stdin
                        docker push $IMAGE:$BUILD_NUMBER
                        docker push $IMAGE:latest
                        docker logout
                    '''
                }
            }
        }
        stage('Test') {
            steps {
                sh '''
                     python3 -m venv --clear venv
                     . venv/bin/activate
                     pip install -q -r requirements.txt
                     pytest --junitxml=results.xml
                '''
    }
    post {
        always {
            junit allowEmptyResults: true, testResults: 'results.xml'
        }
    }
}
    }
}
