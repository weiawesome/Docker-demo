# Docker-Demo
## MySQL Demo
```commandline
docker run --name mysql -e MYSQL_ROOT_PASSWORD=DefaultPassword -e MYSQL_DATABASE=DefaultDb -e MYSQL_USER=DefaultUser -e MYSQL_PASSWORD=DefaultPassword -p 3306:3306 -d mysql:latest
```
> Then you can have the mysql service in localhost:3306
> <br/> Now you can into the container to have the service.

## Flask Demo
```commandline
pip install -r requirements.txt
python main.py
```
> Then you can connect to the mysql service in localhost:3306
> <br/>Furthermore, you can into container to check mysql db status equal to flask-demo.

## Docker Compose Demo
```
# Build image of flask-demo
docker build -t flask-demo .

# Start docker-compose service
docker-compose up -d
```
> Now you can see the service in localhost:8080

## Demo Image
![img.png](img.png)
> Then you can press add 1 or subtract 1 and make influence in mysql container. 