import os
import cv2
import numpy as np
import torch
import torchvision.transforms as transforms
from torchvision import models
from PIL import Image
import requests
from flask import Flask, request, jsonify

# Initialize Flask app
app = Flask(__name__)

# Load pre-trained model (ResNet for image classification, fine-tuned for deforestation detection)
model = models.resnet50(pretrained=True)
num_ftrs = model.fc.in_features
model.fc = torch.nn.Linear(num_ftrs, 2)  # Binary classification: Forest vs. Deforested
model.load_state_dict(torch.load("model.pth", map_location=torch.device('cpu')))
model.eval()

# Image transformation
transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
])

# Function to predict deforestation
def predict_deforestation(image_path):
    image = Image.open(image_path).convert('RGB')
    image = transform(image).unsqueeze(0)
    
    with torch.no_grad():
        output = model(image)
        _, predicted = torch.max(output, 1)
    
    return "Deforestation Detected" if predicted.item() == 1 else "Healthy Forest"

# API endpoint for image upload
@app.route("/predict", methods=["POST"])
def predict():
    if "file" not in request.files:
        return jsonify({"error": "No file provided"}), 400
    
    file = request.files["file"]
    file_path = "temp.jpg"
    file.save(file_path)
    
    result = predict_deforestation(file_path)
    os.remove(file_path)
    
    return jsonify({"prediction": result})

if __name__ == "__main__":
    app.run(debug=True)
