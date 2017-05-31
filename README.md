# Vorgehen
1. `docker network create --driver overlay swt-demo`
2. `docker service create --name redis --network swt-demo redis`
3. `docker service create --update-delay 30s --name backend --replicas 1 --network swt-demo --publish 80:5000 jonadev95/swt-demo`
4. `docker service scale backend=3`
5. `docker service update --image jonadev95/swt-demo-v2 backend`
