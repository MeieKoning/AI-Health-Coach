import torch
from torchvision import transforms
from PIL import Image
import requests
from io import BytesIO

class FoodClassifier:
    def __init__(self, model):
        self.model = model
        self.transform = transforms.Compose([
            transforms.Resize((224, 224)),
            transforms.ToTensor()
        ])

    def classify(self, image_path_or_url):
        if image_path_or_url.startswith("http"):
            response = requests.get(image_path_or_url)
            img = Image.open(BytesIO(response.content)).convert("RGB")
        else:
            img = Image.open(image_path_or_url).convert("RGB")
        input_tensor = self.transform(img).unsqueeze(0)
        with torch.no_grad():
            logits = self.model(input_tensor)
            prediction = torch.argmax(logits, dim=1).item()
        return prediction