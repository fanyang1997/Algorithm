import torch
import torch.nn as nn
import torch.nn.functional as F

class Attention(nn.Module):
    def __init__(self, hidden_dim, is_bi_rnn):
        super(Attention, self).__init__()

        self.hidden_dim = hidden_dim
        self.is_bi_rnn = is_bi_rnn

        if is_bi_rnn:
            self.Q_linear = nn.Linear(2 * hidden_dim, hidden_dim)
            self.K_linear = nn.Linear(2 * hidden_dim, hidden_dim)
            self.V_linear = nn.Linear(2 * hidden_dim, hidden_dim)
        else:
            self.Q_linear = nn.Linear(hidden_dim, hidden_dim)
            self.K_linear = nn.Linear(hidden_dim, hidden_dim)
            self.V_linear = nn.Linear(hidden_dim, hidden_dim)

    def forward(self, inputs, lens):
        size = inputs.size()
        Q = self.Q_linear(inputs)
        K = self.K_linear(inputs)
        V = self.V_linear(inputs)
        
