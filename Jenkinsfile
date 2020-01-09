pipeline 
{
	agent any
	environment 
	{
		install_dir = "/opt/flask-app"
		//ssh_ip = "10.132.0.17"
		//ssh_ip_self = "10.132.0.16"

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
		stage("ssh_into_itself_and_build_project")
		{
			steps
			{
				sh '''ssh ${ssh_ip} << EOF
					ssh ${ssh_ip_self} << EOF
						cd ~/flaskMicroServer
						export BUILD_NUMBER="${number}"
						docker-compose build
						docker-compose push
				'''
			}
		}
		stage("switch_user_to_pythonadm_and_update_service_files")
		{
			steps
			{
				sh '''ssh ${ssh_ip} << EOF
					sudo su - pythonadm << BOB
						cd ${install_dir}
						docker service update --replicas 3 --image jenkins-docker:5000/flask-host:build-${number}
						docker service update --replicas 3 --image jenkins-docker:5000/flask-number:build-${number}
						docker service update --replicas 3 --image jenkins-docker:5000/flask-letter:build-${number}
						docker service update --replicas 3 --image jenkins-docker:5000/flask-sequence:build-${number}
						docker service update --replicas 3 --image jenkins-docker:5000/flask-prize:build-${number}
				'''
			}
		}
	}
}
