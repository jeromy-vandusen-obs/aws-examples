import boto3

ssm = boto3.client("ssm")

simpleText = ssm.get_parameter(Name="PlainTextValue", WithDecryption=False)["Parameter"]["Value"]
secretText = ssm.get_parameter(Name="EncryptedValue", WithDecryption=True)["Parameter"]["Value"]

def lambda_handler(event, context):
    return "Simple Test: %s, Secret Text: %s" %(simpleText, secretText)
