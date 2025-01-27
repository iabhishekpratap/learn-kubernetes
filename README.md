# Learn Kubernetes

Welcome to the **Learn Kubernetes** repository! This repo is designed to help you understand and practice Kubernetes concepts by providing example applications, configurations, and scripts.

---

## Repository Structure

Below is the structure of this repository, along with brief descriptions of its contents:

### **Folders:**

1. **db-demo-app**
   - Contains a sample application to demonstrate the integration of Kubernetes with a database.

2. **express-demo**
   - A demo project showcasing a simple Express.js application.

3. **k8s-konfigs**
   - Includes various Kubernetes configuration files for deploying and managing applications.

4. **node-file-demo**
   - A Node.js demo application that interacts with files, illustrating Kubernetes Persistent Volume usage.

5. **pv-config**
   - Persistent Volume (PV) and Persistent Volume Claim (PVC) configurations for Kubernetes storage management.

6. **testapp**
   - A basic application to test and debug Kubernetes deployments.

### **Files:**

1. **cmd.txt**
   - A text file containing commonly used Kubernetes commands for quick reference.

2. **multi-container-pod.yaml**
   - YAML configuration file for deploying a pod with multiple containers.

3. **my-app-deployment.yml**
   - YAML file for deploying a Kubernetes Deployment for a sample application.

4. **script.py**
   - A Python script for automating or testing Kubernetes-related tasks.

---

## Getting Started

To get started with this repository:

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/learn-kubernetes.git
   cd learn-kubernetes
   ```

2. Review the folder and file structure to understand the examples provided.

3. Use the configuration files (YAML) to create resources in your Kubernetes cluster:
   ```bash
   kubectl apply -f <file-name>
   ```

---

## Prerequisites

- Kubernetes Cluster (Minikube, K3s, or a cloud provider)
- Kubectl installed and configured
- Basic knowledge of Kubernetes concepts (Pods, Deployments, Services, etc.)

---

## Contributing

Feel free to contribute to this repository by:

- Adding new examples
- Fixing issues
- Enhancing existing configurations

Create a pull request with your changes, and ensure they are well-documented.

---

Happy Learning Kubernetes! 🚀

