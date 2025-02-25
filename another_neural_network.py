import torch
import torch.nn as nn

# Create input_tensor with ten features
input_tensor = torch.tensor(
    [[-0.0014,  0.4038,  1.0305,  0.7521, 0.7489, -0.3968,  0.0113, -1.3844, 0.8705, -0.9743]]
)

# Create network with three linear layers 
model = nn.Sequential(  
nn.Linear(10, 18), 
nn.Linear(18, 20), 
nn.Linear(20, 5)  
) 

# Pass input_tensor to model to obtain output 
output_tensor = model(input_tensor) 
print(output_tensor) 