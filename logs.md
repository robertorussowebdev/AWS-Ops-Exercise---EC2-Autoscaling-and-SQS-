# Logs for CloudWatch Alarms and Autoscaling group 

### CloudWatch Scale Out Alarm logs

(these logs comprhend the alarm status for the Scale OUT process, you will see how the process works from the Ok status because of no messages on the queue, to the action state and so Alarm state, where messages are >= 1 and start the action decided on the Autoscaling Group dynamic policy)

**INITIAL STATE OF OK because of no messages on the queue.**

2024-01-12 16:50:12	State update	Alarm updated from OK to In alarm.  

**starting of the alarm because of >= 1 messages on SQS queue**

2024-01-12 16:53:02	Action	Successfully executed action arn:aws:autoscaling:eu-west-2:734873870545:scalingPolicy:8adb436b-553f-44ce-a856-fd2ea832d1cc:autoScalingGroupName/LondonASG:policyName/ScaleOutLondon

**Triggering the action decided from ASG dynamic policy**

2024-01-12 16:58:02	State update	Alarm updated from In alarm to OK.

**status return to ok because of 0 messages on the SQS Queue and threshold is not exceeded < 1**

### CloudWatch Scale In Alarm logs

(these logs comprhend the alarm status for the Scale IN process, you will see how the process works from the Alert status because of no messages on the queue,to OK state, where messages are >= 1 and to the part where messages are deleted and again lower than the threshold of 1(<1) start the action decided on the Autoscaling Group dynamic policy)

2024-01-12 16:50:12	State update	Alarm updated from OK to In alarm.      

**# Initial state of 0 messages on SQS queue**

2024-01-12 16:53:12	State update	Alarm updated from In alarm to OK.      

**>= 1 messages on the queue**

2024-01-12 16:58:12	State update	Alarm updated from OK to In alarm.    

**< 1 messages on the queue**

2024-01-12 16:58:13	Action	Successfully executed action arn:aws:autoscaling:eu-west-2:734873870545:scalingPolicy:eae44ad7-2e3b-4f56-a56d-c4a8fbcfb5cf:autoScalingGroupName/LondonASG:policyName/ScaleInLondon 

**Triggering the action decided from ASG dynamic policy**





## Autoscaling Group logs

## Launching instances logs (because of Scale OUT Action triggering )
Successful	Launching a new EC2 instance: i-0c46cb137083b494e	At 2024-01-11T23:24:02Z a monitor alarm ScaleOut in state ALARM triggered policy ScaleOutLondon changing the desired capacity from 0 to 4. At 2024-01-11T23:24:16Z an instance was started in response to a difference between desired and actual capacity, increasing the capacity from 0 to 4.	2024 January 12, 12:24:18 AM +01:00	2024 January 12, 12:24:50 AM +01:00

Successful	Launching a new EC2 instance: i-0a38188863eb61410	At 2024-01-11T23:24:02Z a monitor alarm ScaleOut in state ALARM triggered policy ScaleOutLondon changing the desired capacity from 0 to 4. At 2024-01-11T23:24:16Z an instance was started in response to a difference between desired and actual capacity, increasing the capacity from 0 to 4.	2024 January 12, 12:24:18 AM +01:00	2024 January 12, 12:24:50 AM +01:00

Successful	Launching a new EC2 instance: i-0c3164675838f1a30	At 2024-01-11T23:24:02Z a monitor alarm ScaleOut in state ALARM triggered policy ScaleOutLondon changing the desired capacity from 0 to 4. At 2024-01-11T23:24:16Z an instance was started in response to a difference between desired and actual capacity, increasing the capacity from 0 to 4.	2024 January 12, 12:24:18 AM +01:00	2024 January 12, 12:24:50 AM +01:00

Successful	Launching a new EC2 instance: i-038918013911b7a4c	At 2024-01-11T23:24:02Z a monitor alarm ScaleOut in state ALARM triggered policy ScaleOutLondon changing the desired capacity from 0 to 4. At 2024-01-11T23:24:16Z an instance was started in response to a difference between desired and actual capacity, increasing the capacity from 0 to 4.	2024 January 12, 12:24:18 AM +01:00


## Terminating instances logs (because of  Scale IN Action triggering)


Successful	Terminating EC2 instance: i-0e9c9add7071518ec	At 2024-01-12T16:58:12Z a monitor alarm ScaleIn in state ALARM triggered policy ScaleInLondon changing the desired capacity from 4 to 0. At 2024-01-12T16:58:21Z an instance was taken out of service in response to a difference between desired and actual capacity, shrinking the capacity from 4 to 0. At 2024-01-12T16:58:21Z instance i-00b23fb3c85171148 was selected for termination. At 2024-01-12T16:58:21Z instance i-00e84bda1190cad10 was selected for termination. At 2024-01-12T16:58:21Z instance i-0c069c382c3a8876a was selected for termination. At 2024-01-12T16:58:21Z instance i-0e9c9add7071518ec was selected for termination.	2024 January 12, 05:58:21 PM +01:00	2024 January 12, 05:59:03 PM +01:00

Successful	Terminating EC2 instance: i-0c069c382c3a8876a	At 2024-01-12T16:58:12Z a monitor alarm ScaleIn in state ALARM triggered policy ScaleInLondon changing the desired capacity from 4 to 0. At 2024-01-12T16:58:21Z an instance was taken out of service in response to a difference between desired and actual capacity, shrinking the capacity from 4 to 0. At 2024-01-12T16:58:21Z instance i-00b23fb3c85171148 was selected for termination. At 2024-01-12T16:58:21Z instance i-00e84bda1190cad10 was selected for termination. At 2024-01-12T16:58:21Z instance i-0c069c382c3a8876a was selected for termination. At 2024-01-12T16:58:21Z instance i-0e9c9add7071518ec was selected for termination.	2024 January 12, 05:58:21 PM +01:00	2024 January 12, 05:59:03 PM +01:00

Successful	Terminating EC2 instance: i-00e84bda1190cad10	At 2024-01-12T16:58:12Z a monitor alarm ScaleIn in state ALARM triggered policy ScaleInLondon changing the desired capacity from 4 to 0. At 2024-01-12T16:58:21Z an instance was taken out of service in response to a difference between desired and actual capacity, shrinking the capacity from 4 to 0. At 2024-01-12T16:58:21Z instance i-00b23fb3c85171148 was selected for termination. At 2024-01-12T16:58:21Z instance i-00e84bda1190cad10 was selected for termination. At 2024-01-12T16:58:21Z instance i-0c069c382c3a8876a was selected for termination. At 2024-01-12T16:58:21Z instance i-0e9c9add7071518ec was selected for termination.	2024 January 12, 05:58:21 PM +01:00	2024 January 12, 05:59:03 PM +01:00

Successful	Terminating EC2 instance: i-00b23fb3c85171148	At 2024-01-12T16:58:12Z a monitor alarm ScaleIn in state ALARM triggered policy ScaleInLondon changing the desired capacity from 4 to 0. At 2024-01-12T16:58:21Z an instance was taken out of service in response to a difference between desired and actual capacity, shrinking the capacity from 4 to 0. At 2024-01-12T16:58:21Z instance i-00b23fb3c85171148 was selected for termination. At 2024-01-12T16:58:21Z instance i-00e84bda1190cad10 was selected for termination. At 2024-01-12T16:58:21Z instance i-0c069c382c3a8876a was selected for termination. At 2024-01-12T16:58:21Z instance i-0e9c9add7071518ec was selected for termination.	2024 January 12, 05:58:21 PM +01:00
