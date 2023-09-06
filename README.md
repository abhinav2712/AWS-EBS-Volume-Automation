# Automated EBS Volume Type Enforcement and Compliance Monitoring System

## Video Demonstartion of the project:
https://github.com/abhinav2712/AWS-EBS-Volume-Automation/assets/68495520/6b0c0ec4-1bbb-42b2-b41e-e17d1c0d4dc6

We can see, first the old volume is deleted and new one is created since the lambda fucntion would get trigerred only on the creation of the new volume. Now on creating a new one, the type is left by default 'GP2', however later on refresh , the type automatically gets converted into 'GP3'


Blog Link: https://abhinavkumar.hashnode.dev/aws-ebs-volume-automation

In today's ever-evolving cloud computing landscape, efficiency and compliance are vital for the smooth operation of any organization's infrastructure. As a Cloud Engineer, it's your responsibility to optimize cloud resources and services while adhering to company policies. This blog explores a unique project that demonstrates the power of automation and monitoring within Amazon Web Services (AWS) to maintain operational excellence and regulatory compliance.

## The Challenge: EBS Volume Type Mismatch
Imagine a scenario where your organization heavily relies on Amazon Elastic Block Store (EBS) volumes, which come in different types. The recurring issue is that team members inadvertently create "GP2" volumes when the company standard is "GP3." This mismatch leads to inefficiencies and poses risks to resources and budgets.

## The Solution: Automation with CloudWatch Events and Lambda
To address this challenge, we leverage two powerful AWS services: Amazon CloudWatch Events and AWS Lambda. These tools enable automatic monitoring of EBS volume creation, detection of "GP2" volumes, and conversion to the preferred "GP3" type, all while maintaining compliance.

## Project Overview
### Step 1: Configure Your AWS Environment
Ensure you have the following prerequisites in place:

AWS account with necessary permissions.
AWS Command Line Interface (CLI).
Basic Python knowledge.

### Step 2: Create a Lambda Function
Create a Lambda function responsible for EBS volume type conversions using the AWS Lambda console. Write Python code to handle GP2 to GP3 conversions.

### Step 3: Set Up a CloudWatch Events Rule
Configure CloudWatch Events to monitor EBS volume creation and trigger the Lambda function when necessary.

### Step 4: Write Lambda Function Logic
Develop Python code to extract volume IDs from ARNs and use boto3 to modify volume types.

## Conclusion
This project showcases the value of automation in maintaining operational excellence and compliance. Whether you're a seasoned Cloud Engineer or new to cloud computing, you can optimize AWS infrastructure while adhering to company standards. By proactively addressing EBS volume type mismatches, you enhance resource utilization and operational efficiency. Automation is a key element in keeping AWS environments well-managed and compliant.

## Detailed BLog on the same:
https://abhinavkumar.hashnode.dev/aws-ebs-volume-automation

