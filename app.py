from flask import Flask, render_template, request, jsonify
from kubernetes import client, config
from Kubefront import Kubefront
from flask_bootstrap import Bootstrap

# app = Flask(__name__)
def create_app():
    app = Flask(__name__)
    Bootstrap(app)

    return app

@create_app.route("/")
def welcome():
    return "Welcome to the Kubefront API!"

@create_app.route("/getnamespaces", methods=['GET'])
def listNamespaces():
    try:
        return jsonify(Kubefront.getNamespaces())

    except FileNotFoundError:
        return 'A kube config was not found in your users profile'
    
    except SyntaxError:
        return 'A syntax error occured in your functions. Please check for any red lines under code in an IDE'

@create_app.route("/getpods", methods=["GET"])
def listPods():
    try:
        return jsonify(Kubefront.getPods())

    except FileNotFoundError:
        return 'A kube config was not found in your users profile'

    except SyntaxError:
        return 'A syntax error occured in your functions. Please check for any red lines under code in an IDE'

@create_app.route("/getdeployments", methods=["GET"])
def listDeployments():
    try:
        return jsonify(Kubefront.getDeployments())

    except FileNotFoundError:
        return 'A kube config was not found in your users profile'

    except SyntaxError:
        return 'A syntax error occured in your functions. Please check for any red lines under code in an IDE'

@create_app.route("/getservices", methods=["GET"])
def listServices():
    try:
        return jsonify(Kubefront.getServices())

    except FileNotFoundError:
        return 'A kube config was not found in your users profile'

    except SyntaxError:
        return 'A syntax error occured in your functions. Please check for any red lines under code in an IDE'

@create_app.route("/getnodes", methods=["GET"])
def listNodes():
    try:
        return jsonify(Kubefront.getNodes())

    except FileNotFoundError:
        return 'A kube config was not found in your users profile'

    except SyntaxError:
        return 'A syntax error occured in your functions. Please check for any red lines under code in an IDE'

create_app.run(port=5000, debug=True)
