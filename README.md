# Kubernetes Python Client Time-Based Scaling App

## Summary: 
This app is a small Python program that makes use of the official client library for Kubernetes to scale the deployment of 
an application. It is intended to be ran within a docker container based off the latest official Python image and Kubernetes 
client library. I have pushed this image to a public repo on my dockerhub (akaja/commerce-scaler:0.0.1) for easy deployment 
via "kubectl run".

## Usage:
1. In scaler.py, set the name, namespace values to match the app you want to scale.
2. Write app logic for the numpods var to match your scaling goals
  a. This app is a simple, contrived scaler that scales the pods the last digit of the current time every minute.
    i. E.g. 2:06 will result in numpods = 6
3. Build the docker image and push to dockerhub.
4. Install via kubectl run or by generating a manifest.

## Out of Box Requirements:
Kubernetes Service Account with access rules:
```yaml
rules:
- apiGroups: ["apps"]
  resources: ["deployments"]
  verbs: ["get", "list", "watch", "create", "update", "patch", "delete"]
```
## Links:
https://github.com/kubernetes-client/python/blob/master/kubernetes/docs/AppsV1Api.md#replace_namespaced_deployment_scale
