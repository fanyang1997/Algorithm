import torch
import torch.nn as nn
import tqdm
import numpy as np
import matplotlib.pyplot as plt


class LogisticRegression(nn.Module):
    def __init__(self, input_size, output_size):
        super(LogisticRegression, self).__init__()
        self.linear = nn.Linear(input_size, output_size)

    def forward(self, x):
        y_pred = torch.sigmoid(self.linear(x))
        return y_pred


epochs = 10000
learning_rate = 0.01
input_dim = 2
output_dim = 1


model = LogisticRegression(input_dim, output_dim)
criterion = nn.BCELoss()
optimizer = torch.optim.SGD(model.parameters(), lr=learning_rate)

losses = []
losses_test = []
Iterations = []
iter = 0

x_train = np.random.rand(100, 2)
x_train = torch.from_numpy(x_train).float()
y_train = np.array([1 if x_train[i][0] + x_train[i][1] > 1 else 0 for i in range(100)])
y_train = torch.from_numpy(y_train).float()

x_test = np.random.rand(100, 2)
x_test = torch.from_numpy(x_test).float()
y_test = np.array([1 if x_test[i][0] + x_test[i][1] > 1 else 0 for i in range(100)])
y_test = torch.from_numpy(y_test).float()


# plt.plot(x_train[y_train == 0, 0], x_train[y_train == 0, 1], 'ro')
# plt.plot(x_train[y_train == 1, 0], x_train[y_train == 1, 1], 'bo')
# plt.show()

for epoch in tqdm.tqdm(range(epochs)):
    x = x_train
    labels = y_train
    optimizer.zero_grad()
    outputs = model(x_train)
    loss = criterion(torch.squeeze(outputs), labels)
    loss.backward()
    optimizer.step()
    iter += 1
    if iter % 100 == 0:
        correct_test = 0
        total_test = 0
        outputs_test = torch.squeeze(model(x_test))
        loss_test = criterion(outputs_test, y_test)
        predicted_test = outputs_test.round().detach().numpy()
        total_test += y_test.size(0)
        correct_test += (predicted_test == y_test.numpy()).sum()
        accuracy_test = correct_test / total_test
        losses_test.append(loss_test.item())
        total = 0
        correct = 0
        total += y_train.size(0)
        correct += (outputs.round().detach().numpy() == y_train.numpy()).sum()
        accuracy = correct / total
        losses.append(loss.item())
        Iterations.append(iter)
        print("Epoch: {}/{}".format(epoch + 1, epochs),
              "| train loss: {:.4f}".format(loss.item()),
              "| test loss: {:.4f}".format(loss_test.item()),
              "| train accuracy: {:.4f}".format(accuracy),
              "| test accuracy: {:.4f}".format(accuracy_test))


print(losses)
print(losses_test)
print(Iterations)