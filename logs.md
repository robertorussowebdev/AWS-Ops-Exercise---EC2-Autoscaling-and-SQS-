#Acrivity for ASG


Not yet in service	Launching a new EC2 instance: i-0603257cbb32045dc	At 2024-01-12T16:42:02Z a monitor alarm ScaleOut in state ALARM triggered policy ScaleOutLondon changing the desired capacity from 0 to 4. At 2024-01-12T16:42:10Z an instance was started in response to a difference between desired and actual capacity, increasing the capacity from 0 to 4.	2024 January 12, 05:42:12 PM +01:00	


Not yet in service	Launching a new EC2 instance: i-038a4300559444706	At 2024-01-12T16:42:02Z a monitor alarm ScaleOut in state ALARM triggered policy ScaleOutLondon changing the desired capacity from 0 to 4. At 2024-01-12T16:42:10Z an instance was started in response to a difference between desired and actual capacity, increasing the capacity from 0 to 4.	2024 January 12, 05:42:12 PM +01:00	


Not yet in service	Launching a new EC2 instance: i-0b279ae291afda364	At 2024-01-12T16:42:02Z a monitor alarm ScaleOut in state ALARM triggered policy ScaleOutLondon changing the desired capacity from 0 to 4. At 2024-01-12T16:42:10Z an instance was started in response to a difference between desired and actual capacity, increasing the capacity from 0 to 4.	2024 January 12, 05:42:12 PM +01:00	


Not yet in service	Launching a new EC2 instance: i-0bf111d85b6f82735	At 2024-01-12T16:42:02Z a monitor alarm ScaleOut in state ALARM triggered policy ScaleOutLondon changing the desired capacity from 0 to 4. At 2024-01-12T16:42:10Z an instance was started in response to a difference between desired and actual capacity, increasing the capacity from 0 to 4.	2024 January 12, 05:42:12 PM +01:00


And then successful

Successful	Launching a new EC2 instance: i-0603257cbb32045dc	At 2024-01-12T16:42:02Z a monitor alarm ScaleOut in state ALARM triggered policy ScaleOutLondon changing the desired capacity from 0 to 4. At 2024-01-12T16:42:10Z an instance was started in response to a difference between desired and actual capacity, increasing the capacity from 0 to 4.	2024 January 12, 05:42:12 PM +01:00	2024 January 12, 05:42:44 PM +01:00


Successful	Launching a new EC2 instance: i-038a4300559444706	At 2024-01-12T16:42:02Z a monitor alarm ScaleOut in state ALARM triggered policy ScaleOutLondon changing the desired capacity from 0 to 4. At 2024-01-12T16:42:10Z an instance was started in response to a difference between desired and actual capacity, increasing the capacity from 0 to 4.	2024 January 12, 05:42:12 PM +01:00	2024 January 12, 05:42:44 PM +01:00


Successful	Launching a new EC2 instance: i-0b279ae291afda364	At 2024-01-12T16:42:02Z a monitor alarm ScaleOut in state ALARM triggered policy ScaleOutLondon changing the desired capacity from 0 to 4. At 2024-01-12T16:42:10Z an instance was started in response to a difference between desired and actual capacity, increasing the capacity from 0 to 4.	2024 January 12, 05:42:12 PM +01:00	2024 January 12, 05:42:44 PM +01:00


Successful	Launching a new EC2 instance: i-0bf111d85b6f82735	At 2024-01-12T16:42:02Z a monitor alarm ScaleOut in state ALARM triggered policy ScaleOutLondon changing the desired capacity from 0 to 4. At 2024-01-12T16:42:10Z an instance was started in response to a difference between desired and actual capacity, increasing the capacity from 0 to 4.	2024 January 12, 05:42:12 PM +01:00



Cloudwatch ScaleOut Alarm
2024-01-12 16:42:02	State update	Alarm updated from OK to In alarm.
2024-01-12 16:42:02	Action	Successfully executed action arn:aws:autoscaling:eu-west-2:734873870545:scalingPolicy:8adb436b-553f-44ce-a856-fd2ea832d1cc:autoScalingGroupName/LondonASG:policyName/ScaleOutLondon
2024-01-12 16:46:02	State update	Alarm updated from In alarm to OK



Cloudwatch ScaleIn Alarm 

2024-01-12 16:42:12	State update	Alarm updated from In alarm to OK.
2024-01-12 16:46:13	Action	Successfully executed action arn:aws:autoscaling:eu-west-2:734873870545:scalingPolicy:eae44ad7-2e3b-4f56-a56d-c4a8fbcfb5cf:autoScalingGroupName/LondonASG:policyName/ScaleInLondon
2024-01-12 16:46:12	State update	Alarm updated from OK to In alarm.
