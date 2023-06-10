import requests
import io
from PIL import Image

API_URL = "https://api-inference.huggingface.co/models/prompthero/openjourney"
API_TOKEN = "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"
headers = {"Authorization": f"Bearer {API_TOKEN}"}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.content

def modelx(prompt):
	image_bytes = query({
		"inputs": prompt,
	})
	image = Image.open(io.BytesIO(image_bytes))
	image.show()

# prompt_text = "spiderman in india"
# visual = modelx(prompt_text)