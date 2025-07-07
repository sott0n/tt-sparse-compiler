import torch


class Add(torch.nn.Module):
    def forward(self, x, y):
        return torch.add(x, y)


add = Add()

X = torch.arange(0, 36).view(6, 6)
Y = torch.arange(36, 72).view(6, 6)
A = torch.tensor(
    [
        [0.0, 1.0, 0.0, 0.0, 0.0, 0.0],
        [0.0, 0.0, 0.0, 0.0, 0.0, 2.0],
        [0.0, 0.0, 0.0, 4.0, 0.0, 0.0],
        [3.0, 0.0, 0.0, 0.0, 0.0, 0.0],
        [0.0, 0.0, 5.0, 0.0, 0.0, 0.0],
        [0.0, 0.0, 0.0, 0.0, 6.0, 0.0],
    ],
    dtype=torch.float32,
)
S = A.to_sparse_csr()

print(add(X, Y))
print(add(S, Y))
print(add(X, S))
print(add(S, S))