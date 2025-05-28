# Serverless Watch Tower
![/Architecture/serverless_watch_tower]()
## Overview

This project provides a robust auto-healing solution for cloud infrastructure using AWS services like Lambda, EventBridge, and IAM Policies. It ensures high availability and resilience for critical components:

- **EC2 Instances**: Automatically restart instances if they fail unexpectedly.
- **Load Balancers**: Remove unhealthy targets automatically.
- **S3 Buckets**: Restore deleted or corrupted files from a backup.

## Features

- **Serverless Architecture**: Built using AWS Lambda for cost efficiency.
- **Event-Driven**: Uses EventBridge for real-time monitoring and automation.
- **Resilience**: Ensures system availability by handling failures automatically.
- **Minimal Configuration**: Simple to set up and deploy.

## Architecture

### Components

- **Amazon EventBridge**: Detects critical events (e.g., EC2 instance failures, unhealthy load balancer targets, S3 file deletions).
- **AWS Lambda**: Executes recovery actions, such as restarting instances, deregistering targets, and restoring files.
- **IAM Policies**: Ensures each Lambda function has appropriate permissions to perform its tasks.
- **Backup S3 Bucket**: Stores critical files for S3 recovery.

### Workflow

1. EventBridge detects a failure or deletion event.
2. Triggers the corresponding Lambda function.
3. The Lambda function executes recovery actions.
4. Logs are generated to monitor the auto-healing process.

## Step-by-Step Setup

### Prerequisites

- AWS account with access to EventBridge, Lambda, IAM, and S3.
- Basic understanding of AWS services.

### Step 1: Set Up S3 Backup Bucket

1. Go to AWS S3 Console.
2. Create a new bucket:
   - **Name**: `global-backup-bucket`.
   - Enable **Versioning** for recovery purposes.

### Step 2: Create EventBridge Rules

#### a. EC2 Auto-Restart Rule

File: `architecture/description.md`

1. Go to EventBridge Console.
2. Create a new rule:
   - **Name**: `EC2AutoRestartRule`.
   - **Event Pattern**: See file for details.
   - **Target**: Lambda function.

#### b. Load Balancer Auto-Healing Rule

File: `src/eventbridge/lb_rule.json`

1. Go to EventBridge Console.
2. Create a new rule:
   - **Name**: `LBAutoHealingRule`.
   - **Event Pattern**: See file for details.
   - **Target**: Lambda function.

#### c. S3 Auto-Restore Rule

File: `src/eventbridge/s3_rule.json`

1. Go to EventBridge Console.
2. Create a new rule:
   - **Name**: `S3AutoRestoreRule`.
   - **Event Pattern**: See file for details.
   - **Target**: Lambda function.

### Step 3: Create Lambda Functions

#### a. EC2 Auto-Restart Lambda

File: `src/lambda/ec2_auto_restart.py`

1. Go to AWS Lambda Console.
2. Create a new function:
   - **Name**: `EC2AutoRestart`.
   - **Runtime**: Python 3.11.
   - Attach an IAM role with the following permissions:
     - File: `src/iam_policies/ec2_policy.json`.

#### b. Load Balancer Auto-Healing Lambda

File: `src/lambda/lb_auto_healing.py`

1. Create a new function:
   - **Name**: `LBAutoHealing`.
   - **Runtime**: Python 3.11.
   - Attach an IAM role with the following permissions:
     - File: `src/iam_policies/lb_policy.json`.

#### c. S3 Auto-Restore Lambda

File: `src/lambda/s3_auto_restore.py`

1. Create a new function:
   - **Name**: `S3AutoRestore`.
   - **Runtime**: Python 3.11.
   - Attach an IAM role with the following permissions:
     - File: `src/iam_policies/s3_policy.json`.

## Monitoring and Testing

- **CloudWatch Logs**: Verify Lambda execution logs in CloudWatch.
- **Simulate Failures**:
  - Stop EC2 instances manually or trigger unhealthy targets in the Load Balancer to test auto-healing.
  - Delete files from an S3 bucket to test restoration.

## Conclusion

This auto-healing solution ensures high availability and resilience for critical AWS resources. By leveraging serverless architecture, it minimizes costs and provides real-time recovery. Extend this solution further with SNS notifications or advanced monitoring tools if needed.

**Enjoy a worry-free cloud infrastructure!** 🚀
