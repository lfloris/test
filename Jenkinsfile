pipeline {

    agent any
    
    def app
    
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
        
            app.inside{
                sh 'echo "Inside the container!"'
            }
            
        }
        
        stage('Push Image') {
            app.push("latest")
        }
        
    }
}
