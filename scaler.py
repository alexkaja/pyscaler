from datetime import datetime
import time
from pprint import pprint
from kubernetes import client, config
from kubernetes.client.rest import ApiException
from kubernetes.client.models.v1_scale_spec import V1ScaleSpec
from kubernetes.client.models.v1_scale import V1Scale
from kubernetes.client.models.v1_object_meta import V1ObjectMeta

def main():
    #load kubernetes configs
    config.load_incluster_config()
    configuration = client.Configuration()
    
    # create an instance of the API class
    api_instance = client.AppsV1Api(client.ApiClient(configuration))
    
    #set name, namespace, and body
    name = 'commerce-nginx' # str | name of the Scale
    namespace = 'default' # str | object name and auth scope, such as for teams and projects
    body = client.V1Scale(
                metadata=V1ObjectMeta(
                    name='commerce-nginx',
                    namespace='default'
                ),
                spec=V1ScaleSpec(
                    replicas=numpods
                )
            )

    #run method with above parameters
    try:
        api_response = api_instance.replace_namespaced_deployment_scale(name, namespace, body)
        print ("Scaling", name, "to", numpods, "pods.") # print how many pods
        pprint(api_response) #uncomment to see api response
    except ApiException as e:
        print("Exception when calling AppsV1Api->replace_namespaced_deployment_scale: %s\n" % e)

#Get starting time to anchor 60 second loop
starttime=time.time()

#start the scaler service loop
while True:
  numpods = datetime.now().minute % 10 # gets numpods as last digit of current time minutes
  if __name__ == '__main__':
    main()
  time.sleep(60.0 - ((time.time() - starttime) % 60.0)) # wait 60 seconds