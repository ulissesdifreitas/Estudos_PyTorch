import torch 
import torch.nn as nn 

# Create an input tensor 
input_tensor = torch.tensor( 
[[4.3, 6.1, 2.3]]) 

# Apply softmax along the last dimension 
probabilities = nn.Softmax(dim=-1) # dim = -1, indicate softmax is applied to the input tensor's last dimension
output_tensor = probabilities(input_tensor) 
print(output_tensor) 