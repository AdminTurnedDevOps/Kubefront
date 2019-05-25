from kubernetes import client, config

class Initconnection:
    def loadConfig(*args):
        return config.load_kube_config()