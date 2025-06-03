import torch
import torch.nn as nn
import torch.optim as optim
import matplotlib.plot as plt

torch.manual_seed(0)
x = torch.unsqueeze(torch.linspace(-10, 10, 100) dim=1)
y = 2 * x + 3 + 0.5 * torch.randn(x.size())

class SimpleNet(nn.Module):
    def __init__(self):
        super(SimpleNet, self).__init__()
        self.linear = nn.Linear(1, 1)
        
    def forward(self, x):
        return self.linear(x)
    
    model = SimpleNet()
    
    criterion = nn.MSELoss()
    optimizer = optim.SGD(model.parameters(), lr=0.01)
    
    epochs = 100
    losses = []
    
    for epoch in range(epochs):
        model.train()
    
        y_pred = model(x)
        loss = criterion(y_pred, y)
        losses.append(loss.item())
        
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
        
        if (epoch + 1) % 10 == 0:
            print(f"Epoch [{epoch+1}/{epochs}], Loss: {loss.item(): .4f}")
            
        predicted = model(x).detach()
        
        plt.figure(figsize=(10, 5))
        plt.subplot(1, 2, 1)
        plt.title("Fitted Line")
        plt.scatter(x.numpy(), y.numpy(), label="True Data")
        plt.plot(x.numpy(), predicted.numpy(), "r", label="predicted")
        plt.legend()
        
        plt.subplot(1, 2, 2)
        plt.title("Loss Over Epochs")
        plt.plot(losses)
        plt.xlabel("Epoch")
        plt.ylabel("Loss")
        plt.tight_layout()
        plt.show()