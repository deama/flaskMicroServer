# Prize-pool Micro Service

References:  
Jenkins: **http://34.77.231.35**  
Flask: **http://35.241.188.21**  
Pytest-coverage: **http://35.241.188.21/coverage**
Trello-board: **https://trello.com/invite/b/s3TUoIxy/739da47e0a94b830e13967d08956fc72/prize-pool-micro-server-plan**  
Presentation: **https://docs.google.com/presentation/d/1k9gB2Yz3MCGR2XEBw6swrBItvSjdaUecSkdbBOl02F0/edit?usp=sharing**
<br><br><br><br><br><br><br><br>


# Original Project Idea
Allow user to play a flappy-bird like game. After completion, the user will be prompted to enter their name and submit their score.

There would be 4 services running, one service would act as the front-end, second service would be the bird, third service would be pip1 and last service would be pip2. If the bird service would break then the game wouldn't really be playable, but if one of the pipes broke, the game would still run, albeit easier.

### Original ERD diagram
![ERD diagram](/images/ERD.png)
There would simply be one table, and it would record the score of the player.

<br>

### Original Use Case Diagram
![use case diagram](/images/UseCase.png)

# What I got
I decided to reduce my scope and make a random prize generator application, wherein the user would generate a random sequence of letters and numbers; the amount of money the user would win would be decided by the analysis of the sequence by the application.

There would be 5 services, first service would be the front-end, second would generate a random number, third would generate a random letter, fourth would generate a random sequence of random numbers and letters, and finally the last service would look at the sequence and decide how much money it is worth.

### New ERD diagram
![ERD new diagram](/images/ERD2.png)
The table would simply store sequences that were generated by the sequence service. This later would be used to check whether the sequence was used or not, disallowing the user to reuse the same sequence.


### New Use Case
![use case diagram](/images/UseCase2.png)


# Testing
Testing was done using pytest and a coverage has also been supplied. Look at *References* for the link to the coverage.  
<br>
60% coverage was achieved.
Could only perform tests on the front-end service as the other services relied upon having requests sent to them.
Coverage may further be increased if integration testing could be performed, such as using Selenium to test the interaction between the services properly.


# Deployment Overview
![techs used](/images/tech.png)
Made a webserver application using Python, MySQL, and Flask. Used git and github for version control whilst using Trello to organise myself. Github would submit requests to Jenkins to update, test using pytest, and redeploy the application. Docker was used to setup an environment for the flask application to run on, ansible was used to setup the VMs that would handle the containers holding the application, and docker-swarm was used to setup rolling updates. Finally, the cloud provider GCP was used to host the application.

Technologies used:  
Python/Mysql/Flask  
Git/Github  
Trello  
Jenkins  
Pytest
Docker/Docker-swarm/docker-compose
Ansible
GCP  

# The Future
Many things could be improved for this flask application, such as adding in a proper design because it is fairly barebones right now. Adding a login feature would be a good as that would allow the user to login and keep track of their winnings progress, as well as compare his winnings to that of others. This would also allow me to prevent the same sequence to be used for the prize picker service as currently if the application goes offline, the database is wiped clean, meaning that the previous sequences aren't saved and therefore cannot be compared to, allowing the user to reuse the same sequences they used before the application was restarted.
