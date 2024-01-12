# AWS Ops Exercise - EC2 Autoscaling and SQS
(Roberto Russo solution) 

**Explanation of the exercise**


This exercise involves setting up an **AWS environment** where **EC2 instances scale based on SQS queue messages**.

-It includes creating an **SQS queue**

-Writing **Python scripts for a message producer (running on your desktop), and a consumer (running on EC2 instances)**.

-Additionally, it involves setting up **an EC2 Auto Scaling group** with the **consumer script** in its **launch template bootstrap process**  and testing the **scale-out/in mechanism based on the queue's message load.**

# Prerequisites:
- A clean AWS CLI environment where you have already set your Access Keys.

- IAM Role with the necessary SQS access policies for sending and receiving messages for EC2 instances.

- A standard Amazon SQS Queue.

- A Key Pair for EC2 instances.

- A Public Amazon S3 Bucket. Ensure that the bucket has the appropriate GetObject policy applied.

- Python scripts for Producer and Consumer: Producer.py should be on your desktop, and Consumer.py should be in a bucket to make it downloadable on your EC2 instances.

- An Autoscaling Group with Scaling Policies attached to Amazon CloudWatch Alarms.

- A Launch Template.

- Two CloudWatch Alarms for Scale Out and Scale In processes.

# Step 1: Check for your AWS CLI
Make sure you have a **Command Line Interface (CLI)** installed on your **desktop**; 

it is a mandatory requirement to launch the **producer script from the desktop** and gain access to the AWS environment.

- To verify this, open your **Command Prompt** and enter:

  ```
  aws --version
  aws configure get aws_access_key_id
  aws configure get aws_secret_access_key
  ```
![cmd AWS CLI check ](Screenshots/cmdcheck.png)

If the prompt returns your access key credentials, it means you have already set them, and therefore, you have access to AWS resources.

Let's continue with the exercise.

# Step 2: Create a Standard SQS Queue

Now, let's create your Amazon SQS Queue.

- Open your AWS Console Home and use the search bar to find '**SQS**.' Click on the 'Simple Queue Service' result.
- In the SQS dashboard, navigate to **Create queue**.
- Enter the **Name** as 'MyQueue,' leave the other settings as defaults, and then click on **Create queue**. p.s. I setted MyQueue,but you can use every name you want for all the exercise.

![cmd AWS CLI check ](Screenshots/sqs2.png)

Set your SQS Queue Name and then leave all settings as defaults.



![cmd AWS CLI check ](Screenshots/sqsfinal.png)


Final result → You created your SQS Queue


# Step 3: Create a IAM Role for EC2 instances

1. Navigate to **IAM > Roles** and click on **Create role**.
2. Select **EC2** under use case and click **Next**.
3. Leave all options at their defaults and click **Next**.
4. Provide a Name for your Role and then click **Create Role**.
5. Once the Role is created, go to **Role > Permissions > Add Permissions > Create Inline Policy**.
6. In the Create Inline Policy, choose JSON, and replace the existing JSON policy with the following.
7. Click **Next** and then **Save Changes**.
8. Add a **Policy Name**.
9. You have successfully created your IAM Role and attached the SQS policy!



