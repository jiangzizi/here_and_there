import matplotlib.pyplot as plt

# 训练日志数据
training_logs = [
    {'loss': 10.4, 'learning_rate': 0.0002, 'epoch': 0.07},
    {'loss': 7.6063, 'learning_rate': 0.0002, 'epoch': 0.14},
    {'loss': 7.0125, 'learning_rate': 0.0002, 'epoch': 0.21},
    {'loss': 6.6562, 'learning_rate': 0.0002, 'epoch': 0.28},
    {'loss': 5.7156, 'learning_rate': 0.0002, 'epoch': 0.35},
    {'loss': 4.7094, 'learning_rate': 0.0002, 'epoch': 0.42},
    {'loss': 4.0219, 'learning_rate': 0.0002, 'epoch': 0.49},
    {'loss': 3.4438, 'learning_rate': 0.0002, 'epoch': 0.56},
    {'loss': 3.0797, 'learning_rate': 0.0002, 'epoch': 0.63},
    {'loss': 2.8656, 'learning_rate': 0.0002, 'epoch': 0.7},
    {'loss': 2.6344, 'learning_rate': 0.0002, 'epoch': 0.77},
    {'loss': 2.4859, 'learning_rate': 0.0002, 'epoch': 0.84}
]

# 提取损失值和迭代轮数
loss_values = [log['loss'] for log in training_logs]
epochs = [log['epoch'] for log in training_logs]

# 绘制损失图像
plt.plot(epochs, loss_values, marker='o', linestyle='-')
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.title('Training Loss')
plt.grid(True)
plt.show()
