# Machine Learning Practice

This repository contains the code that I create in my deliberate practice sessions to enhance my skills.

## Currently I am learning:
1. Pytorch 
2. Python Best Practices 
3. Object Oriented Programming in Python
4. Github actions
5. Docker

## Latest Updates:
1. ML Model Deployment using Flask.

To check the model, please use the following command.

```python
python DeploymentWeb/app.py
```

2. ML Model Deployment using Streamlit.

To check the model, please use the following command.

```python
python -m streamlit run DeploymentStreamlit\app.py
```

3. ML Model Deployment using Docker

First, change the directory to "docker_app".
Run the following commands. 

```python
docker build -t ml_app_docker . 
```

Once the container is up and running, run following command,

```python
docker container run -p 5000:5000 ml_app_docker    
```
