🧠 Cloud-Based Medical QA System
AWS-Integrated Machine Learning Project
📋 Project Overview
This project demonstrates a cloud-deployed Machine Learning (ML) application built for answering medical-related questions using a fine-tuned QA model. The system leverages AWS services to ensure scalability, accessibility, and secure management of data and infrastructure.
The model was trained and deployed on an Amazon EC2 instance, with data securely stored in an Amazon S3 bucket. Access permissions were managed using AWS IAM (Identity and Access Management).
☁️ AWS Services Used
🔐 1. AWS Identity and Access Management (IAM)
Purpose:
IAM was used to create and manage secure access permissions for different AWS resources.
Created a custom IAM user/role with limited access to S3 and EC2.
Followed the principle of least privilege, ensuring minimal security risks.
Used IAM to manage credentials safely for local access testing.
Alternative (Not Implemented):
AWS Secrets Manager for automatic credential rotation.
Reason: Not necessary for small-scale academic deployment and would increase complexity and cost.
🗃️ 2. Amazon S3 (Simple Storage Service)
Purpose:
S3 was used for storing the cleaned_medquad.csv dataset, providing a reliable, cloud-based data source for the ML model.
The dataset was uploaded manually to an S3 bucket.
Used as a centralized data storage solution.
Alternative (Not Implemented):
Direct programmatic access using Boto3 SDK to read from S3 within the EC2 app.
Reason: For demonstration purposes, manual upload was sufficient, and integration was skipped to focus on showcasing AWS services setup.
💻 3. Amazon EC2 (Elastic Compute Cloud)
Purpose:
EC2 was used to host and run the ML model and Gradio interface.
A t2.medium Ubuntu instance was configured for deployment.
The Flask/Gradio app was executed and tested successfully via public URL.
Verified end-to-end model functionality.
Alternative (Not Implemented):
AWS Lambda or AWS SageMaker for serverless or managed ML hosting.
Reason: EC2 was sufficient for this scale and provided better control over dependencies.
🚀 Deployment Flow
Dataset uploaded to S3 bucket
IAM role created for secure access management
EC2 instance launched and configured
ML application (Gradio/Flask-based) deployed and tested
Logs and results verified on terminal and Gradio public link
🧩 Tech Stack
Backend: Python (Flask, Gradio)
Cloud: AWS EC2, S3, IAM
Libraries: Pandas, Transformers, Scikit-learn
Dataset: Medical QA Dataset (cleaned_medquad.csv)
📸 Screenshots
📁 Screenshots are available in the /screenshots folder.
IAM Roles and Permissions
S3 Bucket with Uploaded Dataset
EC2 Instance Configuration
Terminal Log (Model Running Successfully)
Gradio Interface Screenshot
⚙️ Future Integration
Planned upgrades for the next version:
Automate dataset retrieval using Boto3
Integrate IAM role-based S3 access into code
Deploy the model using AWS SageMaker for managed ML
Store model responses in Amazon RDS for persistence
🧹 Resource Management
All AWS resources (EC2, IAM, and S3) have been safely terminated after deployment testing to prevent unnecessary billing.
👨‍💻 Author
Aaditya Arvind Ramrame
Cloud and Machine Learning Enthusiast
📧 [Your Email Here]
🔗 [GitHub Profile Link]
