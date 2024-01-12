import boto3
import json


region = 'eu-west-3' # Replace 'REGION'  with your AWS region 
queue_name = 'MyQueue' # Replace 'QUEUE_NAME' with your  SQS queue name


sqs = boto3.client('sqs', region_name=region) # Create an SQS client

# JSON message content -> I'll use the exercise example
message_payload = {
    "vehicleId": "VH2001",
    "make": "Honda",
    "model": "Civic",
    "year": 2020,
    "color": "Blue",
    "mileage": 15000
}

# Send message to your SQS queue
queue_url = sqs.get_queue_url(QueueName=queue_name)['QueueUrl']
response = sqs.send_message(
    QueueUrl=queue_url,
    MessageBody=json.dumps(message_payload)
)
# Display the correct message sending with his MessageId connected
print(f"Message sent. MessageId: {response['MessageId']}")