# cloud-engineer-assessment

## Project Overview

This project was developed as part of the Cloud Engineer Junior technical assessment for Siddhan Intelligence.

The objective of the project was to build and deploy a simple Python Flask web application on an AWS EC2 instance with public HTTP access. The infrastructure configuration is included using Terraform, and a GitHub Actions workflow is configured to automate Continuous Integration (CI) by validating the application whenever changes are pushed to the GitHub repository.

The project demonstrates fundamental cloud engineering concepts, including application deployment, Infrastructure as Code (IaC), version control, IAM-based access management, and CI automation using GitHub Actions.


## Technologies Used

| Category                     | Technology                |
| ---------------------------- | ------------------------- |
| Cloud Provider               | Amazon Web Services (AWS) |
| Compute Service              | Amazon EC2                |
| Operating System             | Amazon Linux              |
| Programming Language         | Python 3                  |
| Web Framework                | Flask                     |
| Infrastructure as Code       | Terraform                 |
| Version Control              | Git                       |
| Repository Hosting           | GitHub                    |
| CI/CD                        | GitHub Actions            |
| Identity & Access Management | AWS IAM                   |
| Development Environment      | Visual Studio Code        |






## Repository Structure

```text
cloud-engineer-assessment/
│
├── app.py
├── requirements.txt
├── README.md
├── architecture-diagram.png
├── .gitignore
├── .github/
│   └── workflows/
│       └── deploy.yml
└── terraform/
    ├── provider.tf
    ├── variables.tf
    ├── main.tf
    └── outputs.tf
```

The repository is organized into three main components:

* **Application** – Contains the Flask web application and its dependencies.
* **Terraform** – Contains the Infrastructure as Code (IaC) configuration used to provision AWS resources.
* **GitHub Actions** – Contains the CI workflow that automatically validates the application whenever changes are pushed to the `main` branch.



## Deployment Steps

### Step 1: Launch an EC2 Instance

* Created an Amazon EC2 instance running **Amazon Linux** in the **us-east-1** region.
* Attached an **IAM Role (Instance Profile)** to the EC2 instance.
* Configured a **Security Group** with an **All TCP** inbound rule to simplify testing during the assessment. In a production environment, inbound access would be restricted to only the required ports.

### Step 2: Connect to the EC2 Instance

Connected to the EC2 instance using SSH and the downloaded key pair.

```bash
ssh -i "assign.key.pem" ec2-user@44.202.83.202
```

### Step 3: Clone the Repository

```bash
git clone https://github.com/AshutoshRana-7/cloud-engineer-assessment.git
cd cloud-engineer-assessment
```

### Step 4: Install Dependencies

```bash
sudo dnf install python3 git -y
pip3 install -r requirements.txt
```

### Step 5: Run the Flask Application

```bash
python3 app.py
```

The application can be accessed through the EC2 public IP:

```text
http://<EC2_PUBLIC_IP>:5000
```

### Step 6: Continuous Integration

A GitHub Actions workflow is configured to run automatically whenever changes are pushed to the **main** branch. The workflow performs the following tasks:

* Checks out the repository
* Sets up the Python environment
* Installs the project dependencies
* Validates the Flask application

This Continuous Integration (CI) workflow helps ensure that the application can be built successfully after every code change.



## Design Decisions

The following design decisions were made during the implementation of this project:

* **AWS EC2** was selected as the deployment platform because the assessment required hosting the application on a Virtual Machine with public HTTP access.

* **Python Flask** was chosen as the web framework due to its lightweight architecture and simplicity, making it suitable for deploying a basic web application.

* **Terraform** was used to demonstrate Infrastructure as Code (IaC), enabling infrastructure configuration to be managed in a version-controlled and reproducible manner.

* **GitHub Actions** was implemented to provide a simple Continuous Integration (CI) pipeline that automatically validates the application whenever code is pushed to the repository.

* **IAM Role** was attached to the EC2 instance to demonstrate secure AWS access management without embedding credentials within the application.


## Trade-offs Considered

While building this project, I made a few decisions to keep the implementation simple while still meeting the assessment requirements.

* I used the Flask development server instead of a production web server such as Gunicorn or Nginx because the goal was to demonstrate application deployment rather than production hosting.

* The application is deployed on a single EC2 instance, which keeps the architecture simple and cost-effective. In a production environment, multiple instances with a load balancer would be a better choice for high availability.

* For easier testing during development, the Security Group was configured with an **All TCP** inbound rule. In a real-world deployment, only the required ports would be opened to improve security.

* The GitHub Actions workflow focuses on Continuous Integration by validating the application whenever changes are pushed to the repository. Automatic deployment to EC2 was intentionally left out to keep the pipeline simple and aligned with the scope of this assessment.


## Cost Awareness

While building this project, I considered the cost of the AWS resources used.

* A single Amazon EC2 instance was used to keep the infrastructure simple and minimize costs.
* Existing AWS services such as IAM Roles and Security Groups were used, which do not incur additional charges.
* The EC2 instance was stopped when not in use to avoid unnecessary compute costs.
* The project was designed for demonstration purposes, so only the required resources were created without adding extra services such as Load Balancers or Auto Scaling Groups.

This approach keeps the overall deployment simple, cost-effective, and aligned with the requirements of the assessment.





## Author

**Ashutosh Rana**  
Cloud Engineer Junior Candidate

- **Education:** B.Tech in Computer Science and Engineering
- **GitHub:** https://github.com/AshutoshRana-7
