
node {

    def app

        stage('Clone Repository'){
                echo "Cloning repository..."
                checkout scm

        }
        
        stage('Build') {

                echo 'Building..'
                docker.build("mypython")
                app.push("latest")

        }
        
        stage('Test') {

                echo 'Test...'
            
        }

}
