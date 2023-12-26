pipeline {
    agent any

    environment {
        DOCKER_REGISTRY_CREDS = 'docker-hub'
        EMAIL_NOTIFICATION = 'sp20-bcs-038@cuiatk.edu.pk'
        DOCKER_BFLASK_IMAGE = 'sp20bcs038399/flask-web-app' // 
    }

    stages {
        stage('Build') {
            steps {
                sh 'docker build -t flask-web-app .'
                sh "docker tag my-flask-app ${DOCKER_BFLASK_IMAGE}"
            }
        }

        stage('Test') {
            steps {
                sh 'docker run flask-web-app python -m pytest app/tests/'
            }
        }

        stage('Deploy') {
            steps {
                script {
                    withCredentials([usernamePassword(credentialsId: "${DOCKER_REGISTRY_CREDS}", passwordVariable: 'DOCKER_PASSWORD', usernameVariable: 'DOCKER_USERNAME')]) {
                        sh "echo \$DOCKER_PASSWORD | docker login -u \$DOCKER_USERNAME --password-stdin docker.io"
                        sh "docker push ${DOCKER_BFLASK_IMAGE}"

                        sh "docker pull ${DOCKER_BFLASK_IMAGE}:latest"
                        sh "docker stop flask-web-app || true"
                        sh "docker rm flask-web-app || true"

                        try {
                            sh "docker run -d -p 80:5000 --name flask-web-app ${DOCKER_BFLASK_IMAGE}:latest"
                        } catch (Exception e) {
                            currentBuild.result = 'FAILURE'
                            error("Deployment failed. Rolling back to the previous version.")
                        }
                    }
                }
            }
        }
    }

    post {
        failure {
            emailext body: 'The deployment of Flask App failed. Please check the Jenkins console for details.',
                     subject: 'Flask App Deployment Failed',
                     to: "${EMAIL_NOTIFICATION}"
        }

        always {
            sh 'docker logout'
        }
    }
}
