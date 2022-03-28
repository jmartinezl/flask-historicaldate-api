# flask-historicaldate-api
Basic Python Flask app in Docker which gives historical events by date from Wikipedia API

### Build application
Build the Docker image manually by cloning the Git repo.
```
$ git clone https://github.com/jmartinezl/flask-historicaldate-api.git
$ docker build -t jmartinezl/flask-historicaldate-api .
```

### Using Docker Compose
You can also use the docker-compose file
```
docker compose up
```

### Download precreated image
You can also just download the existing image from [DockerHub](https://hub.docker.com/r/jmartinezl/flask-historicaldate-api/).
```
docker pull jmartinezl/flask-historicaldate-api
```

### Run the container
Create a container from the image.
```
$ docker run --name my-container -d -p 5000:5000 jmartinezl/flask-historicaldate-api
```

Now visit http://localhost:5000
```
 The hostname of the container is 6095273a4e9b and its IP is 172.17.0.2. 
```

### Verify the running container
Verify by checking the container ip and hostname (ID):
```
$ docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' my-container
172.17.0.2
$ docker inspect -f '{{ .Config.Hostname }}' my-container
6095273a4e9b
```


