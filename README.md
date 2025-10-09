# 🧠 **Cloud-Based Medical QA System**
### ☁️ *AWS-Integrated Machine Learning Project*

---

## 📋 **Project Overview**
This project demonstrates a **cloud-deployed Machine Learning (ML)** application built to answer **medical-related questions** using a fine-tuned QA model.  
The system leverages **AWS services** to ensure **scalability**, **accessibility**, and **secure management** of data and infrastructure.

The model was trained and deployed on an **Amazon EC2** instance, with data securely stored in an **Amazon S3** bucket.  
Access permissions and security were managed using **AWS IAM (Identity and Access Management)**.

---

## ☁️ **AWS Services Used**

### 🔐 **1. AWS Identity and Access Management (IAM)**
**Purpose:**
- 🧾 Created and managed secure access permissions for different AWS resources.  
- 👤 Configured a custom IAM user/role with limited access to S3 and EC2.  
- 🛡️ Followed the principle of *least privilege* to ensure minimal security risks.  
- 🔑 Used IAM for safe credential management during local access testing.  

**Alternative (Not Implemented):**
- 🧰 *AWS Secrets Manager* for automatic credential rotation.  

**Reason:** Not necessary for small-scale academic deployment and would increase complexity and cost.

---

### 🗃️ **2. Amazon S3 (Simple Storage Service)**
**Purpose:**
- ☁️ Used for storing the `cleaned_medquad.csv` dataset, providing a reliable, cloud-based data source for the ML model.  
- 📤 The dataset was uploaded manually to an S3 bucket.  
- 🗂️ Served as a centralized, secure data storage solution.  

**Alternative (Not Implemented):**
- 🔗 Direct programmatic access using the **Boto3 SDK** to read data from S3 within the EC2 app.  

**Reason:** For demonstration purposes, manual upload was sufficient, and integration was skipped to focus on showcasing AWS setup.

---

### 💻 **3. Amazon EC2 (Elastic Compute Cloud)**
**Purpose:**
- 🚀 Used to host and run the ML model and **Gradio interface**.  
- ⚙️ Configured a `t2.medium` Ubuntu instance for deployment.  
- 🧩 Executed Flask/Gradio app and tested successfully via public URL.  
- 🔍 Verified full model functionality and response generation.  

**Alternative (Not Implemented):**
- 🪶 *AWS Lambda* or *AWS SageMaker* for serverless or managed ML hosting.  

**Reason:** EC2 was ideal for this scale and provided better control over dependencies and environment setup.

---

## 🚀 **Deployment Flow**
1. 🧺 Dataset uploaded to **S3 bucket**  
2. 🔐 IAM role created for **secure access management**  
3. 💻 **EC2 instance** launched and configured  
4. 🤖 ML application (Flask + Gradio) deployed and tested  
5. 📈 Logs and results verified on **terminal and Gradio public link**

---

## 🧩 **Tech Stack**
| Layer | Tools & Technologies |
|-------|----------------------|
| 🧠 **Backend** | Python (Flask, Gradio) |
| ☁️ **Cloud** | AWS EC2, S3, IAM |
| 🧰 **Libraries** | Pandas, Transformers, Scikit-learn |
| 📊 **Dataset** | Medical QA Dataset (`cleaned_medquad.csv`) |

---

## 📸 **Screenshots**
📁 Available in the `/screenshots` folder:  
1. 🧑‍💻 IAM Roles and Permissions  
2. 🪣 S3 Bucket with Uploaded Dataset  
3. 💻 EC2 Instance Configuration  
4. 🧾 Terminal Log (Model Running Successfully)  
5. 🌐 Gradio Interface Screenshot  

---

## ⚙️ **Future Integration**
Planned upgrades for the next version:
1. 🤖 Automate dataset retrieval using **Boto3**  
2. 🔐 Integrate **IAM role-based S3 access** into code  
3. 🧱 Deploy the model using **AWS SageMaker** for managed ML  
4. 💾 Store model responses in **Amazon RDS** for persistence  

---

## 🧹 **Resource Management**
All AWS resources (**EC2**, **IAM**, and **S3**) have been **safely terminated** after testing to prevent unnecessary billing.  

---

## 👨‍💻 **Author**
**Aaditya Arvind Ramrame**  
🌩️ *Cloud and Machine Learning Enthusiast*  
📧 [aadityaramrame@gmail.com](mailto:aadityaramrame@gmail.com)  
🔗 [GitHub Profile](https://github.com/Aadityaramrame)

---
⭐ *“Bringing Machine Learning to the Cloud — One Service at a Time.”* ☁️
