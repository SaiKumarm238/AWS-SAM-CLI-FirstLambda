import time
import os

def simple_types(event, context):
    print(event)
    return event

def list_types(event, context):
    print(event)
    student_score = {"Sai": 100, "kumar":90, "Manikonda":100}
    scores = []
    for name in event:
        scores.append(student_score[name])
    return scores

def dict_types(event, context):
    print(event["Sai"])
    return event


def lambda_handler(event, context):   
    print("Lambda function ARN:", context.invoked_function_arn)
    print("CloudWatch log stream name:", context.log_stream_name)
    print("CloudWatch log group name:",  context.log_group_name)
    print("Lambda Request ID:", context.aws_request_id)
    print("Lambda function memory limits in MB:", context.memory_limit_in_mb)
    # We have added a 1 second delay so you can see the time remaining in get_remaining_time_in_millis.
    #time.sleep() 
    print("Lambda time remaining in MS:", context.get_remaining_time_in_millis())
    print(os.getenv("restapiurl"))
    print(os.getenv("dbname"))