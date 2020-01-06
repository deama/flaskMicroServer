pipeline 
{
	agent any
	environment 
	{
		install_dir = "/opt/flask-app"
		ssh_ip = "34.76.175.152"
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
		stage("switch_user_to_pythonadm_and_setup_docker-compose") 
		{
			steps 
			{
				sh '''ssh ${ssh_ip} << EOF
					sudo su - pythonadm << BOB
						cd ${install_dir}
						docker-compose up -d --build
				'''
			}
		}
	}
}
