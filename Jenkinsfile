pipeline 
{
	agent any
	environment 
	{
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
		stage("setup_docker-compose") 
		{
			steps 
			{
				sh '''ssh ${ssh_ip} << EOF
					cd ~/flaskMicroServer
					docker-compose up -d --build
				'''
			}
		}
	}
}
