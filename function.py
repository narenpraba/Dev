import json
import boto3
import constant as ct
client = boto3.client('ssm')
sns = boto3.client("sns", region_name="us-east-1")
ssm = boto3.client("ssm", region_name="us-east-1")
def send_sns_success():
    success_sns_arn = ssm.get_parameter(Name=ct.SUCCESSNOTIFICATIONARN, WithDecryption=True)["Parameter"]["Value"]
    component_name = constant.COMPONENT_NAME
    env = ssm.get_parameter(Name=constant.ENVIRONMENT, WithDecryption=True)['Parameter']['Value']
    success_msg = ct.SUCCESS_MSG
    sns_message = (f"{component_name} :  {success_msg}")
    print(sns_message, 'text')
    succ_response = sns.publish(TargetArn=success_sns_arn,Message=json.dumps({'default': json.dumps(sns_message)}),
        Subject= env + " : " + component_name,MessageStructure="json")
    return succ_response
    
def lambda_handler(event, context):
    # TODO implement
    try :
        send_sns_success()
        print('done')
    except Exception as e:
        print("error")
    
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }