# import requests
import json


# def first_lambda(event, context):
#     return {
#         "statusCode": 200,
#         "body": json.dumps({
#             "message": "Aws Lambda is Super Cool"
#         }),
#     }

def first_lambda(event, context):
    return "Hello "+ event