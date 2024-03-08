import boto3
import json

bedrock = boto3.client(service_name="bedrock-runtime")

#Message API format
body = json.dumps({
  "max_tokens": 256,
  "messages": [{"role": "user", "content": "Hello"}],
  "anthropic_version": "bedrock-2023-05-31"
})

#Call the claude3 on the Amazon Bedrock
response = bedrock.invoke_model(body=body, modelId="anthropic.claude-3-sonnet-20240229-v1:0")

#Extract the response content in the json
response_body = json.loads(response.get("body").read())
print(response_body.get("content"))
