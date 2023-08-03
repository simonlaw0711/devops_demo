minikube start
eval $(minikube docker-env)
docker build -t fastapi-app:v1 .
kubectl apply -f k8s/
kubectl port-forward service/fastapi-app 8080:8080