# bedrock-api-access
Create demo code examples to request Claude 3 models on the Bedrock

Install Boto3 before running the scripts.
```
pip3 install boto3
```

## 1. Chat with Claude 3 on Amazon Bedrock in Text  <br />
   This is the script to chat with Claude 3 on Amazon Bedrock. Change the value of "content" at line 9 to what you would like to ask the LLM.
   Run the script by:
   ```
   python claude3-text.py
   ```
## 2. Analyze image by Claude 3 on Amazon Bedrock  <br />
   This is the script to get the captions for an image with Claude 3 on Amazon Bedrock. Change the path of the image you'd like to feed at line 44.
   Change the LLM prompt to instruct how you would like to process the image at line 23, the value of the key "text".
   Run the script by:
   ```
   python claude3-image.py
   ```
## 3.List all the available Claude 3 Models  <br />
   This is the script to get all the available Anthropic models on the Amazon Bedrock.
   Run the script by:
   ```
   python modellist.py
   ```

## 4. Create a Side-Scrolling Game  <br />
   This is the script to utilize Claude 3 Opus on Amazon Bedrock to develop a Side-Scrolling browser game, the sample code is based on the Claude 3 Opus examples provided by Amazon Bedrock. The script defines the prompt and generates the source code of the game, users can open the game directly in the web browser.
   you can refer to this [Article](https://community.aws/content/2fvcf7pytefRYGPtkRpCaqwXcl5/get-started-with-claude-3-opus-on-amazon-bedrock-quickly-through-real-world-use-cases) to know more about the case.
   ```
   python modellist.py
   ```
   The screenshot of the game:
   ![image](https://github.com/szl0144/bedrock-api-access/assets/40918217/9acfd1b8-70a0-4012-a530-3ec77cdc0c0e)

