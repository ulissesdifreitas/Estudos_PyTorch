import torch
import torch.nn as nn

# Create input_tensor with three features
input_tensor = torch.tensor([
    [0.3471, 0.4547, -0.2356]
])

# Define our first linear layer
linear_layer = nn.Linear(
    in_features=3,
    out_features=2
)

# Pass input through linear layer
output = linear_layer(input_tensor)
print(output)

weight = linear_layer.weight
bias = linear_layer.bias

print(weight)
print(bias)