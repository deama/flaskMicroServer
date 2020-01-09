pipeline 
{
	agent any
	environment 
	{
		install_dir = "/opt/flask-app"
		ssh_ip = "10.132.0.17"
		ssh_ip_self = "10.132.0.16"
		number = "${env.BUILD_NUMBER}"
	}

	stages 
	{
		stage("setup_git_repo")
		{
			steps
			{
				sh '''ssh ${ssh_ip} << EOF
					cd ~/
					sudo rm -r ./flaskMicroServer
					git clone --single-branch --branch master https://github.com/deama/flaskMicroServer.git
					sudo apt update
				'''
			}
		}
		stage("setup_directory")
        {
            steps
            {
                sh '''ssh ${ssh_ip} << EOF
					cd ~/flaskMicroServer
                    sudo rm -rf ${install_dir}
					sudo mkdir ${install_dir}
					sudo cp -r ./* ${install_dir}
					sudo chown -R pythonadm:pythonadm ${install_dir}
                '''
            }
        }
		stage("ssh_into_itself_and_git_clone")
		{
			steps 
			{
				sh '''ssh ${ssh_ip} << EOF
                    cd ~/
                    sudo rm -r ./flaskMicroServer
                    git clone --single-branch --branch master https://github.com/deama/flaskMicroServer.git
                '''
			}
		}
		stage("ssh_into_itself_and_build_project")
        {
            steps
            {
				sh '''ssh ${ssh_ip} << EOF
					cd ~/flaskMicroServer
					docker-compose build
					docker-compose push
                '''
            }
        }
		stage("switch_user_to_pythonadm_and_run_local_registry")
        {
            steps
            {
                sh '''ssh ${ssh_ip} << EOF
                    sudo su - pythonadm << BOB
                        cd ${install_dir}
						docker rm -f registry
                        docker run -d --name registry -v registry:/var/lib/registry -p 5000:5000 registry:2
                '''
            }
        }
		stage("switch_user_to_pythonadm_and_deploy_stack")
        {
            steps
            {
                sh '''ssh ${ssh_ip} << EOF
                    sudo su - pythonadm << BOB
                        cd ${install_dir}
						sed -i "24d" docker-compose.yaml
						sed -i "24i \  image: jenkins-docker:5000/flask-host:build-${number}" docker-compose.yaml
						sed -i "38d" docker-compose.yaml
                        sed -i "38i \  image: jenkins-docker:5000/flask-number:build-${number}" docker-compose.yaml
						sed -i "44d" docker-compose.yaml
                        sed -i "44i \  image: jenkins-docker:5000/flask-letter:build-${number}" docker-compose.yaml
						sed -i "50d" docker-compose.yaml
                        sed -i "50i \  image: jenkins-docker:5000/flask-sequence:build-${number}" docker-compose.yaml
						sed -i "55d" docker-compose.yaml
                        sed -i "55i \  image: jenkins-docker:5000/flask-prize:build-${number}" docker-compose.yaml
						docker stack deploy --compose-file docker-compose.yaml proj
                '''
            }
        }
	}
}
