import torch 
import torch.nn as nn

input_tensor = torch.tensor([[6.0]]) 
sigmoid = nn.Sigmoid()  
output = sigmoid(input_tensor) 

print(output)

# Activation function as the last layer
model = nn.Sequential(
    nn.Linear(6, 4), # First linear layer
    nn.Linear(4, 1), # Second linear layer
    nn.Sigmoid()
)