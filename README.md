# Steps for demonstration
```
docker network create --driver overlay swt-demo
docker service create --name redis --network swt-demo redis
docker service create --update-delay 30s --name backend --replicas 1 --network swt-demo --publish 80:5000 jonadev95/swt-demo
docker service scale backend=3
docker service update --image jonadev95/swt-demo-v2 backend
docker service update --rollback --update-delay 0s
