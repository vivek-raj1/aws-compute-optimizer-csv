# aws-compute-optimizer-csv
Automate the retrieval of AWS Compute Optimizer recommendations for EC2 instances and EBS volumes, and store the results in CSV files. This Python script streamlines the process, making it easy to analyze and optimize your AWS resources based on Compute Optimizer suggestions. Enhance your cloud efficiency with actionable insights.

This Python script interacts with AWS Compute Optimizer to retrieve EC2 instance and EBS volume recommendations and stores them in CSV files.

## Prerequisites

- AWS CLI configured with necessary permissions.
- Python 3.x installed.
- Boto3 library installed (`pip install boto3`).

## Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/vivek-raj1/aws-compute-optimizer-csv.git

   ```
2. **Install dependencies:**
    ```
    pip install boto3
    ```
3. **Configure AWS credentials:**
    ```
    aws configure
    ```
    Ensure that the configured AWS CLI profile has the necessary permissions for Compute Optimizer.

## Usage
Run the script using Python:
```
python compute_optimizer_recommendations.py
```
This will retrieve EC2 instance and EBS volume recommendations from Compute Optimizer and create CSV files accordingly.

## Configuration
Adjust the following parameters in the script as needed:
- AWS CLI profile ()
- AWS region (region_name)

## CSV Files
`ec2_compute_optimizations.csv`: Contains EC2 instance recommendations.
`ebs_compute_optimizations.csv`: Contains EBS volume recommendations.