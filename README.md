## Predicitive Modelling for Semiconductor Manufacturing

This project focuses on using machine learning techniques to predict the quality of semiconductor manufacturing processes based on the SECOM dataset. Accurate prediction of manufacturing quality is crucial for optimizing production, reducing waste, and ensuring the reliability of semiconductor products. By employing machine learning algorithms, this project aims to predict semiconductor manufacturing outcomes accurately based on relevant features such as sensory data and manufacturing parameters.

### Objective:
The primary objective of this project is to develop reliable prediction models that accurately forecast the quality of semiconductor manufacturing processes. These models will assist manufacturers in understanding and improving their production processes, ultimately leading to higher quality products and reduced costs.

### Dataset:
The project utilizes the SECOM dataset, which contains relevant attributes such as sensory measurements and process parameters from semiconductor manufacturing. This dataset serves as the foundation for training and evaluating the machine learning models.

### Techniques:
Machine learning algorithms and techniques explored in this project include:
- Support Vector Classifier

### Evaluation:
The performance of the models is evaluated using metrics such as accuracy, precision, and f1-score. Techniques such as cross-validation and hyperparameter tuning are employed to enhance the models' reliability and applicability across different manufacturing conditions.

![image](https://github.com/user-attachments/assets/d169b0d8-527b-44cd-b9ce-5482d497dbe3)

---

### PROJECT STRUCTURE:

![image](https://github.com/user-attachments/assets/d12e2265-3480-4f71-8a03-56afc5351ee6)


---

### FINAL OUTPUT:

https://github.com/user-attachments/assets/083e2886-5231-4bdd-a355-496b669b1ffa

---

## AWS-CICD-Deployment-with-Github-Actions:
### 1. Login to AWS console.
### 2. Create IAM (Identity Access Manager) user for deployment.

    1. EC2 access : It is virtual machine

    2. ECR: Elastic Container registry to save your docker image in aws

    #Description: About the deployment

    1. Build docker image of the source code

    2. Push your docker image to ECR

    3. Launch Your EC2 

    4. Pull Your image from ECR in EC2

    5. Lauch your docker image in EC2


    #Policy:

    1. AmazonEC2ContainerRegistryFullAccess

    2. AmazonEC2FullAccess

### 3. Create ECR repo to store/save docker image
    - Save the URI: 566373416292.dkr.ecr.us-east-1.amazonaws.com/semiconductor

### 4. Create EC2 machine (Ubuntu)

### 5. Open EC2 and Install docker in EC2 Machine:

    sudo apt-get update -y

    sudo apt-get upgrade

    #required

    curl -fsSL https://get.docker.com -o get-docker.sh

    sudo sh get-docker.sh

    sudo usermod -aG docker ubuntu

    newgrp docker

### 6. Configure EC2 as self-hosted runner:
    setting>actions>runner>new self hosted runner> choose os> then run command one by one

### 7. Setup github secrets:

    AWS_ACCESS_KEY_ID=

    AWS_SECRET_ACCESS_KEY=

    AWS_REGION = us-east-1

    AWS_ECR_LOGIN_URI = demo>>  566373416292.dkr.ecr.ap-south-1.amazonaws.com

    ECR_REPOSITORY_NAME = simple-app
      




