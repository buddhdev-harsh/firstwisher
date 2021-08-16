pipeline {
    agent any 
        environment {
            registry = "harshdevl/wisher"
            registryCredential = 'Docker'
        }
        stages {
            stage ('checking out from github') {
                steps {
                    checkout([$class: 'GitSCM', branches: [[name: '*/master']], extensions: [], userRemoteConfigs: [[credentialsId: 'harshdevl', url: 'git@github.com:harshdevl/firstwisher.git']]])
                }
            }
            stage ('building Docker image...') {
                steps {
                    script {
                        dockerImage = docker.build registry + ":$BUILD_NUMBER" 
                    }
                }
            }
            stage ('pushing docker image...'){
                steps {
                    script {
                        docker.withRegistry('',registryCredential) {
                            dockerImage.push()
                        }
                    }
                }
            }
            stage ('cleaning up...') {
                steps {
                    sh "docker rmi $registry:$BUILD_NUMBER"
                }
            }
        }
    post {
        always {
            mail bcc: '', body: "See ${BUILD_URL}", cc: 'harahismast@gmail.com', from: '', replyTo: '', subject: "Jenkins: ${JOB_NAME}: Build status is ${currentBuild.currentResult}", to: 'ht50159@gmail.com'
            cleanWs()
        }
    }
    
}
