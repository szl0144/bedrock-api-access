import boto3
import json
import re

# Define the prompt
prompt = "[{\"type\":\"text\",\"text\":\"Write me a fully complete web app as a single HTML file. The app should contain a simple side-scrolling game where I use WASD to move around.  When moving around the world, occasionally the character/sprite will encounter words. When a word is encountered, the player must correctly type the word as fast as possible.The faster the word is successfully typed, the more point the player gets. We should have a counter in the top-right to keep track of points. Words should be random and highly variable to keep the game interesting. \\n\\nYou should make the website very aesthetic and use Tailwind.\"}]"

# Initialize the Bedrock client
bedrock = boto3.client(service_name="bedrock-runtime",region_name="us-west-2")

#Define Claude 3 Message API
body = json.dumps({
  "max_tokens": 4096,
  "messages": [{"role": "user", "content": prompt}],
  "anthropic_version": "bedrock-2023-05-31"
})

#Invoke Claude 3 Opus on the Amazon Bendrcok
response = bedrock.invoke_model(contentType="application/json", body=body, modelId="anthropic.claude-3-opus-20240229-v1:0")

#Extract API Response
response_body = json.loads(response.get("body").read())
content = response_body.get("content")[0].get('text', '')

#Get the HTML code from the response
pattern = r'```html(.*?)```'
match = re.search(pattern, content, re.DOTALL)
content_html = match.group(1).strip()

# Write the code into game.html
with open('game.html', 'w') as file:
    file.write(content_html)
