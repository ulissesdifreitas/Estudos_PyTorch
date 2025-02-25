import torch

list = [[1,2,3], [4,5,6]]

# to load from list
tensor = torch.tensor(list)

# tensor attribute
shaper = tensor.shape

# tensor data type
type = tensor.dtype

# tensor device
device = tensor.device


print(tensor)
print(shaper)
print(type)
print(device)

