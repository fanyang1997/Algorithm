import torch
import numpy as np
from torch import nn
import torch.autograd.profiler as profiler


class MyModel(nn.Module):
    def __init__(self, in_features: int, out_features: int,
                 bias: bool = True):
        super(MyModel, self).__init__()
        self.linear = nn.Linear(in_features, out_features, bias)

    def forward(self, input, mask):
        with profiler.record_function("linear_forward"):
            output = self.linear(input)

        with profiler.record_function("mask indicates"):
            threshold = output.sum(axis=1).mean().item()
            hi_idx = np.argwhere(mask.cpu().numpy() > threshold)
            hi_idx = torch.from_numpy(hi_idx)

        return output, hi_idx


if __name__ == "__main__":
    model = MyModel(500, 10)
    input = torch.randn(128, 500)
    mask = torch.randn(500, 500, 500)

    model(input, mask)

    with profiler.profile(with_stack=True, profile_memory=True) as prof:
        out, idx = model(input, mask)
    print(prof.key_averages(group_by_stack_n=5).table(sort_by="cpu_time_total", row_limit=10))
