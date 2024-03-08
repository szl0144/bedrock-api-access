import json
import boto3
import base64

bedrock = boto3.client(service_name="bedrock-runtime")

def call_claude_sonet(base64_string):
    prompt_config = {
        "anthropic_version": "bedrock-2023-05-31",
        "max_tokens": 4096,
        "messages": [
            {
                "role": "user",
                "content": [
                    {
                        "type": "image",
                        "source": {
                            "type": "base64",
                            "media_type": "image/png",
                            "data": base64_string,
                        },
                    },
                    {"type": "text", "text": "Provide a caption for this image, give me the insights"},
                ],
            }
        ],
    }

    body = json.dumps(prompt_config)

    modelId = "anthropic.claude-3-sonnet-20240229-v1:0"
    accept = "application/json"
    contentType = "application/json"

    response = bedrock.invoke_model(
        body=body, modelId=modelId, accept=accept, contentType=contentType
    )
    response_body = json.loads(response.get("body").read())

    results = response_body.get("content")[0].get("text")
    return results
  
if __name__ == "__main__":
  image_path = 'pax2.jpeg'
  # 读取图片，转换为Base64
  with open(image_path, 'rb') as image_file:
      image_data = image_file.read()
      base64_string = base64.b64encode(image_data).decode('utf-8')
      
  caption = call_claude_sonet(base64_string)
  print(caption)