pipeline 
{
	agent any
	environment 
	{
		install_dir = "/opt/flask-app"
		ssh_ip = "app-docker"
		ssh_ip_self = "jenkins-docker"
		number = "${env.BUILD_NUMBER}"
	}

	stages 
	{
		stage("setup_git_repo")
		{
			steps 
			{
				sh '''ssh -o StrictHostKeyChecking=no ${ssh_ip} << EOF
				'''
			}
		}
		stage("setup_directory")
		{
			steps
			{
				sh '''ssh -o StrictHostKeyChecking=no ${ssh_ip} << EOF
					cd ~/flaskMicroServer
					sudo rm -rf ${install_dir}
					sudo mkdir ${install_dir}
					sudo cp -r ./* ${install_dir}
					sudo chown -R pythonadm:pythonadm ${install_dir}
				'''
			}
		}
		stage("ssh_into_itself_and_build_project")
		{
			steps
			{
				sh '''ssh -o StrictHostKeyChecking=no ${ssh_ip_self} << EOF
					cd ~/flaskMicroServer
					export BUILD_NUMBER="${number}"
					docker-compose build
					docker-compose push
				'''
			}
		}
		stage("update_service_files")
		{
			steps 
			{
				sh '''ssh -o StrictHostKeyChecking=no ${ssh_ip} << EOF
					cd ${install_dir}
					docker service update --replicas 3 --image jenkins-docker:5000/flask-host:build-${number} proj_flask-host
					docker service update --replicas 3 --image jenkins-docker:5000/flask-number:build-${number} proj_flask-number
					docker service update --replicas 3 --image jenkins-docker:5000/flask-letter:build-${number} proj_flask-letter
					docker service update --replicas 3 --image jenkins-docker:5000/flask-sequence:build-${number} proj_flask-sequence
					docker service update --replicas 3 --image jenkins-docker:5000/flask-prize:build-${number} proj_flask-prize
				'''
			}
		}
	}
}
