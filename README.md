# bedrock-api-access
Create demo code examples to request Claude 3 models on the Bedrock

Install Boto3 before running the scripts.
```
pip3 install boto3
```

1. claude3-text.py
   This is the script to chat with Claude 3 on Amazon Bedrock. Change the value of "content" at line 9 to what you would like to ask the LLM.
   Run the script by:
   ```
   python claude3-text.py
   ```
2. claude3-image.py
   This is the script to get the captions for an image with Claude 3 on Amazon Bedrock. Change the path of the image you'd like to feed at line 44.
   Change the LLM prompt to instruct how you would like to process the image at line 23, the value of the key "text".
   Run the script by:
   ```
   python claude3-image.py
   ```
4. modellist.py
   This is the script to get all the available Anthropic models on the Amazon Bedrock.
   Run the script by:
   ```
   python modellist.py
   ```
   
