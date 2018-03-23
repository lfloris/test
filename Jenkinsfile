pipeline {

    environment{
        def app
    }
    
    agent any
    
    stages {
        
        stage('Clone Repository'){
            steps{
                echo "Cloning repository..."
                checkout scm
            }
        }
        
        stage('Build') {
            steps {
                echo 'Building..'
                app = docker.build("test/Dockerfile")
            }
        }
        
        stage('Test') {
            
            steps{
                app.inside{
                    sh 'echo "Inside the container!"'
                }
            }
            
        }
        
        stage('Push Image') {
            steps{
                app.push("latest")
            }
        }
        
    }
}
