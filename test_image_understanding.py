from PIL import Image
from transformers import AutoProcessor, Blip2ForConditionalGeneration
import torch

image = Image.open('test_openai_ultra_happy_assistant.jpg')


processor = AutoProcessor.from_pretrained("Salesforce/blip2-opt-2.7b")
model = Blip2ForConditionalGeneration.from_pretrained("Salesforce/blip2-opt-2.7b", torch_dtype=torch.float16)
model.half()#optimize 
device = "cuda" if torch.cuda.is_available() else "cpu"
model.to(device)


inputs = processor(image, return_tensors="pt").to(device, torch.float16)

generated_ids = model.generate(**inputs, max_new_tokens=20)
generated_text = processor.batch_decode(generated_ids, skip_special_tokens=True)[0].strip()
print(generated_text)
