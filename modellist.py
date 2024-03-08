import boto3

bedrock = boto3.client(service_name="bedrock")
response = bedrock.list_foundation_models(byProvider="anthropic")

for summary in response["modelSummaries"]:
    print(summary["modelId"])