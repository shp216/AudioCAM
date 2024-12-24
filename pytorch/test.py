import torch

# Path to the saved .pt file
file_path = "AudioCAM/bowling3.pt"

# Load the .pt file
cam_tensor = torch.load(file_path)

# Print the shape of the loaded tensor
print(f"Loaded CAM tensor shape: {cam_tensor.shape}")
