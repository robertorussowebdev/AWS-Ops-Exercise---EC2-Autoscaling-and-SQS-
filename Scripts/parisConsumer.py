import boto3
import json
import time

region = 'eu-west-3' # Replace 'REGION'  with your AWS region 
queue_name = 'MyQueue' # Replace 'QUEUE_NAME' with your  SQS queue name



sqs = boto3.resource('sqs', region_name=region) # Create an SQS client
queue = sqs.get_queue_by_name(QueueName=queue_name)

# While loop for process, display, delete and wait messages

while True:
    messages = queue.receive_messages(MaxNumberOfMessages=1, WaitTimeSeconds=20)

    for message in messages:
        # Process the message content and display it
        content = json.loads(message.body)
        print(f"Processing message: {content}")

        # Delete the message from the queue after processing it
        message.delete()

    #  Adding a wait for one minute before polling for messages again
    time.sleep(60)