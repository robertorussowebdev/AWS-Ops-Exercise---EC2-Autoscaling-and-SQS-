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

![SQS Name ](Screenshots/sqs2.png)

Set your SQS Queue Name and then leave all settings as defaults.



![SQS Queue Check  ](Screenshots/sqsfinal.png)


Final result → You created your SQS Queue


# Step 3: Create a IAM Role for EC2 instances

1. Navigate to **IAM > Roles** and click on **Create role**.
2. Select **EC2** under use case and click **Next**.
3. Leave all options at their defaults and click **Next**.
4. Provide a Name for your Role and then click **Create Role**.
5. Once the Role is created, go to **Role > Permissions > Add Permissions > Create Inline Policy**.
6. In the Create Inline Policy, choose JSON, and replace the existing JSON policy with the following.
```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "Stmt1704991352140",
      "Action": [
        "sqs:DeleteMessage",
        "sqs:ReceiveMessage",
        "sqs:SendMessage"
      ],
      "Effect": "Allow",
      "Resource": "*"
    }
  ]
}
```
   
7. Click **Next** and then **Save Changes**.
8. Add a **Policy Name**.
9. You have successfully created your IAM Role and attached the SQS policies!


![IAM Role creation ](Screenshots/iam3.png)
Select EC2 under Use Case

![IAM Role creation ](Screenshots/iam5.png)
Create a Name for your Role and leave all settings as defaults.
![IAM Role creation ](Screenshots/iam6.png)
Once the Role is created, go to **Role > Permissions > Add Permissions > Create Inline Policy**.
![IAM Role creation ](Screenshots/iam7.png)

![IAM Role creation ](Screenshots/iampolicy.png)
In the Create Inline Policy, choose JSON, and replace the existing JSON policy with the following and then save, you have done all here.

# Extra step: Simulate the policy
An extra step, but it's a **best practice** to do so, is to **simulate the policy**.

For this reason, let's go to the **Amazon Policy Simulator** and test the role. Filter by the SQS service, and in the actions, select **DeleteMessage, SendMessage, ReceiveMessage**.

![IAM Policy Simulation](Screenshots/simul.png)
Select your Role, service SQS and the actions said before.

![IAM Policy Simulation](Screenshots/simul2.png)
As you can see, action are allowed so it's all OK.

# Step 4: Create a key pair

1. Navigate to **EC2 > Key Pairs** (under Network & Security).
2. Click on **Create key pair**.
3. Enter **Name** as `paris`. (In your setup, give it any name you prefer)
4. Click on **Create Key Pair**.
5. Download the Key and save it to your PC.

![IAM Policy Simulation](Screenshots/key3.png)









