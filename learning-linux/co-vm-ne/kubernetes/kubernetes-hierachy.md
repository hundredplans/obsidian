[Minikube](minikube)
    [Kubernetes](what-is-kubernetes)
        [Cluster](kubernetes-cluster.md)
            [Master Node](control-plane.md)/[Control-plane](control-plane) -> Developer (via API Server with [[kubectl]])
                [API Server](kubernetes-API-server)
                [Scheduler](kubernetes-scheduler) -> API Server
                [Controller Manager](kubernetes-controller-manager)
                [Cloud Controller Manager](kubernetes-cloud-controller-manager) (Optional)
                [Database - etcd](etcd)
				    [Secrets](kubernetes-secrets)
            [Worker Node](worker-node)/s -> Users (via Kube-proxy), Master Node (via Kubelet)
                [Kubelet](kubelet.md) -> API Server
                [Container Runtime](kubernetes-container-runtime) (Docker)
                [Service](kubernetes-service) (Optional)
                    [Pod](pod.md)
                        [Container](container)
                        Container2
                        Container3
                    Pod
                    Pod
                [Addons](kubernetes-addons)
                [Kube Proxy](kube-proxy)
            Worker Node2
		    Worker Node3
        Cluster
            Master Node
            Worker Node2
            Worker Node3

Software to run Kubernetes
Kubernetes Software
Cluster Layer
Node Layer
Service Layer
Service Component Layer