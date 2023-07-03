[Minikube](minikube.md)
    [Kubernetes](what-is-kubernetes.md)
        [Cluster](kubernetes-cluster.md)
            [Master Node](control-plane.md)/[Control-plane](control-plane.md) -> Developer (via API Server with [[kubectl]])
                [API Server](kubernetes-API-server.md)
                [Scheduler](kubernetes-scheduler.md) -> API Server
                [Controller Manager](kubernetes-controller-manager.md)
                [Cloud Controller Manager](kubernetes-cloud-controller-manager.md) (Optional)
                [Database - etcd](etcd.md)
				    [Secrets](kubernetes-secrets.md)
            [Worker Node](worker-node.md)/s -> Users (via Kube-proxy), Master Node (via Kubelet)
                [Kubelet](kubelet.md) -> API Server
                [Container Runtime](kubernetes-container-runtime.md) (Docker)
                [Service](kubernetes-service.md) (Optional)
                    [Pod](pod.md)
                        [Container](container.md)
                        Container2
                        Container3
                    Pod
                    Pod
                [Addons](kubernetes-addons.md)
                [Kube Proxy](kube-proxy.md)
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