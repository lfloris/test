
node {

    def app

        stage('Clone Repository'){
                echo "Cloning repository..."
                checkout scm

        }
        
        stage('Build') {

                echo 'Building..'
                docker.build("test/Dockerfile")
                app.push("latest")

        }
        
        stage('Test') {

                echo 'Test...'
            
        }

}
