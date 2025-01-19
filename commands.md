## Jenkins master
https://github.com/devopsjourney1/jenkins-101
https://www.jenkins.io/doc/book/installing/docker/

- docker build -t jenkins-video ./jenkins-master
- docker network create jenkins-video-net
- docker run --name jenkins-video --restart=on-failure --ip 172.20.0.1 --detach --network jenkins-video-net --env DOCKER_HOST=tcp://docker:2376 --env DOCKER_CERT_PATH=/certs/client --env DOCKER_TLS_VERIFY=1 --publish 8081:8080 --publish 50001:50000 --volume jenkins-vid-data:/var/jenkins_home --volume jenkins-vid-docker-certs:/certs/client:ro jenkins-video


## Jenkins cloud
docker run --name socat-proxy -d --restart=always --ip 172.20.0.2 -p 127.0.0.1:2376:2375 --network jenkins -v /var/run/docker.sock:/var/run/docker.sock alpine/socat tcp-listen:2375,fork,reuseaddr unix-connect:/var/run/docker.sock



## Jenkins agent

## Terraform
- terraform init
- terraform apply
- terraform destroy