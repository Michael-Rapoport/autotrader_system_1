# mlops/model_deployment.py
import mlflow

def deploy_model(model, model_name, model_version, mlflow_tracking_uri):
   mlflow.set_tracking_uri(mlflow_tracking_uri)
   
   with mlflow.start_run():
       mlflow.log_param('model_name', model_name)
       mlflow.log_param('model_version', model_version)
       mlflow.keras.log_model(model, 'model')
       
       model_uri = f"models:/{model_name}/{model_version}"
       mlflow.register_model(model_uri, model_name)

