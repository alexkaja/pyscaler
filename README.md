# Kubernetes Python Client Time-Based Scaling App

## Summary: 
This app is a small Python program that makes use of the [official client library](https://github.com/kubernetes-client/python) for Kubernetes to scale the deployment of 
an application. It is intended to be ran within a docker container based off the latest official Python image and Kubernetes 
client library. I have pushed this image to a public repo on my dockerhub (akaja/commerce-scaler:0.0.1) for easy deployment 
via "kubectl run".

## Usage:
1. In scaler.py, set the name, namespace values to match the app you want to scale.
* The dockerhub image cited above has these values coded as "commerce" and "default", respectively.
* If you use my image, you'll need to exec into the pod and edit the scaler.py file inside to match your evironment.

```python
 #set name, namespace, and body
 name = 'your_app_name' # str | name of the Scale
 namespace = 'your_namespace' # str | object name and auth scope, such as for teams and projects
```
2. Write app logic for the numpods var to match your scaling goals.
* This app is a simple, contrived scaler that scales the pods the last digit of the current time, every minute.
* E.g. 2:06 will result in numpods = 6
3. Build the docker image and push to dockerhub.
4. Install via _kubectl run_ or by generating a manifest / helm chart.

## Out of Box Requirements:
The _.load_incluster_config()_ method automatically gives the application access to the default service acount; however, you will still need to grant further permissions:
```yaml
rules:
- apiGroups: ["apps"]
  resources: ["deployments"]
  verbs: ["get", "list", "watch", "create", "update", "patch", "delete"]
```
## Links:
https://github.com/kubernetes-client/python/blob/master/kubernetes/docs/AppsV1Api.md#replace_namespaced_deployment_scale
