🧠 Cloud-Based Medical QA System

AWS-Integrated Machine Learning Project

📋 Project Overview

This project demonstrates a cloud-deployed Machine Learning (ML) application built for answering medical-related questions using a fine-tuned QA model. The system leverages AWS services to ensure scalability, accessibility, and secure management of data and infrastructure.
The model was trained and deployed on an Amazon EC2 instance, with data securely stored in an Amazon S3 bucket. Access permissions were managed using AWS IAM (Identity and Access Management).

☁️ AWS Services Used

🔐 1. AWS Identity and Access Management (IAM)

Purpose:

1. IAM was used to create and manage secure access permissions for different AWS resources.
2. Created a custom IAM user/role with limited access to S3 and EC2.
3. Followed the principle of least privilege, ensuring minimal security risks.
4. Used IAM to manage credentials safely for local access testing.

Alternative (Not Implemented):

1.AWS Secrets Manager for automatic credential rotation.
Reason: Not necessary for small-scale academic deployment and would increase complexity and cost.

🗃️ 2. Amazon S3 (Simple Storage Service)

Purpose:

1. S3 was used for storing the cleaned_medquad.csv dataset, providing a reliable, cloud-based data source for the ML model.

2. The dataset was uploaded manually to an S3 bucket.

3. Used as a centralized data storage solution.

Alternative (Not Implemented):

1. Direct programmatic access using Boto3 SDK to read from S3 within the EC2 app.
Reason: For demonstration purposes, manual upload was sufficient, and integration was skipped to focus on showcasing AWS services setup.

💻 3. Amazon EC2 (Elastic Compute Cloud)

Purpose:

1. EC2 was used to host and run the ML model and Gradio interface.
2. A t2.medium Ubuntu instance was configured for deployment.
3. The Flask/Gradio app was executed and tested successfully via public URL.
4. Verified end-to-end model functionality.

Alternative (Not Implemented):
1. AWS Lambda or AWS SageMaker for serverless or managed ML hosting.
Reason: EC2 was sufficient for this scale and provided better control over dependencies.

🚀 Deployment Flow

1. Dataset uploaded to S3 bucket
2. IAM role created for secure access management
3. EC2 instance launched and configured
4. ML application (Gradio/Flask-based) deployed and tested
5. Logs and results verified on terminal and Gradio public link

🧩 Tech Stack
1. Backend: Python (Flask, Gradio)
2. Cloud: AWS EC2, S3, IAM
3. Libraries: Pandas, Transformers, Scikit-learn
4. Dataset: Medical QA Dataset (cleaned_medquad.csv)

📸 Screenshots
📁 Screenshots are available in the /screenshots folder.
1. IAM Roles and Permissions
2. S3 Bucket with Uploaded Dataset
3. EC2 Instance Configuration
4. Terminal Log (Model Running Successfully)
5. Gradio Interface Screenshot

⚙️ Future Integration
1. Planned upgrades for the next version:
2. Automate dataset retrieval using Boto3
3. Integrate IAM role-based S3 access into code
4. Deploy the model using AWS SageMaker for managed ML
5. Store model responses in Amazon RDS for persistence

🧹 Resource Management
All AWS resources (EC2, IAM, and S3) have been safely terminated after deployment testing to prevent unnecessary billing.

👨‍💻 Author

Aaditya Arvind Ramrame

Cloud and Machine Learning Enthusiast

📧 aadityaramrame@gmail.com

🔗 https://github.com/Aadityaramrame
