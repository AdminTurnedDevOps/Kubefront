from kubernetes import client, config
import Initconnection
import Logging
from more_itertools import unique_everseen 

class Kubefront:

    def getDeployments():
        Initconnection.Initconnection.loadConfig()
        k8s_beta = client.ExtensionsV1beta1Api()
        Logging.Logging.log('Retrieving Deployments')
        getDeployments = k8s_beta.list_deployment_for_all_namespaces()
        output = []
        for deployment in getDeployments.items:
            if deployment is None:
                Logging.Logging.log('No deployments found')
            else:
                output.append(f'{deployment.metadata.name} {deployment.status}')

        return list(unique_everseen(output))

    def getNamespaces():
        Initconnection.Initconnection.loadConfig()
        apiV1 = client.CoreV1Api()
        Logging.Logging.log('Retrieving Namespaces')
        nameSpaces = apiV1.list_pod_for_all_namespaces(watch=False)
        output = []
        for nameSpace in nameSpaces.items:
            output.append(nameSpace.metadata.namespace)

        return list(unique_everseen(output))

    def getPods():
        Initconnection.Initconnection.loadConfig()
        apiV1 = client.CoreV1Api()
        Logging.Logging.log('Retrieving pods')
        ret = apiV1.list_pod_for_all_namespaces(watch=False)
        output = []
        for pod in ret.items:
            if pod is None:
                Logging.Logging.log('Pods were not found')
            else:
                output.append(pod.metadata.name)

        return list(unique_everseen(output))

    def getServices():
        Initconnection.Initconnection.loadConfig()
        Logging.Logging.log('Retrieving Services')
        apiV1 = client.CoreV1Api()
        services = apiV1.list_service_for_all_namespaces()
        output = []
        for service in services.items:
            if service is None:
                Logging.Logging.log('No services found')
            else:
                output.append(f'{service.metadata.name}')

        return list(unique_everseen(output))