
node {

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
                docker.build("test/Dockerfile")
                app.push("latest")
            }
        }
        
        stage('Test') {
            
            steps{
                echo 'Test...'
            }
            
        }
        
        
    }
}
