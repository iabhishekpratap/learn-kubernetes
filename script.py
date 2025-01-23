# Description: A script to delete services in a Kubernetes cluster.
# script to delete services in kubernetes cluster

import subprocess

def delete_services(service_names):
    """
    Deletes the specified Kubernetes services by their names.

    Args:
        service_names (list): A list of service names to delete.

    Returns:
        None
    """
    for service in service_names:
        try:
            print(f"Deleting service: {service}")
            result = subprocess.run([
                "kubectl", "delete", "service", service
            ], capture_output=True, text=True, check=True)
            print(result.stdout)
        except subprocess.CalledProcessError as e:
            print(f"Failed to delete service {service}: {e.stderr}")

if __name__ == "__main__":
    # List of service names to delete
    services_to_delete = [
        "my-nginx",
        "my-webapp",
        "node-app"
    ]

    delete_services(services_to_delete)
