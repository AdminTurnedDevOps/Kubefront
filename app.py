from flask import Flask, render_template, request, jsonify
from kubernetes import client, config
from Kubefront import Kubefront

app = Flask(__name__)

@app.route("/")
def welcome():
    return "Welcome to the Kubefront API!"

@app.route("/getnamespaces", methods=['GET'])
def listNamespaces():
    try:
        return jsonify(Kubefront.getNamespaces())

    except FileNotFoundError:
        return 'A kube config was not found in your users profile'
    
    except SyntaxError:
        return 'A syntax error occured in your functions. Please check for any red lines under code in an IDE'

@app.route("/getpods", methods=["GET"])
def listPods():
    try:
        return jsonify(Kubefront.getPods())

    except FileNotFoundError:
        return 'A kube config was not found in your users profile'

    except SyntaxError:
        return 'A syntax error occured in your functions. Please check for any red lines under code in an IDE'

@app.route("/getdeployments", methods=["GET"])
def listDeployments():
    try:
        return jsonify(Kubefront.getDeployments())

    except FileNotFoundError:
        return 'A kube config was not found in your users profile'

    except SyntaxError:
        return 'A syntax error occured in your functions. Please check for any red lines under code in an IDE'

@app.route("/getservices", methods=["GET"])
def listServices():
    try:
        return jsonify(Kubefront.getServices())

    except FileNotFoundError:
        return 'A kube config was not found in your users profile'

    except SyntaxError:
        return 'A syntax error occured in your functions. Please check for any red lines under code in an IDE'

app.run(port=5000, debug=True)
