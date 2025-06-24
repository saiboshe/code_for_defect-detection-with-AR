import numpy as np
import matplotlib.pyplot as plt

# 定义 epoch 数组，从 0 到 600
epochs = np.linspace(0, 600, 601)

# 定义一个函数，用于模拟训练损失随 epoch 衰减的过程
def simulate_loss(initial, converged, k, epochs):
    return converged + (initial - converged) * np.exp(-k * epochs)

# 设置每个模型的初始和收敛损失，以及衰减率（k）
# 参数仅为估计值，用于模拟曲线
yolov8_loss       = simulate_loss(initial=1.5, converged=0.35, k=0.005, epochs=epochs)
yolov5_loss       = simulate_loss(initial=1.7, converged=0.45, k=0.005, epochs=epochs)
ssd_loss          = simulate_loss(initial=2.0, converged=0.65, k=0.005, epochs=epochs)
faster_rcnn_loss  = simulate_loss(initial=2.5, converged=0.8, k=0.005, epochs=epochs)
efficientdet_loss = simulate_loss(initial=1.5, converged=0.35, k=0.005, epochs=epochs)

# 绘制训练损失对比曲线
plt.figure(figsize=(10, 6))
plt.plot(epochs, yolov8_loss, label='YOLOv8', linewidth=2)
plt.plot(epochs, yolov5_loss, label='YOLOv5', linewidth=2)
plt.plot(epochs, ssd_loss, label='SSD', linewidth=2)
plt.plot(epochs, faster_rcnn_loss, label='Faster R-CNN', linewidth=2)
plt.plot(epochs, efficientdet_loss, label='EfficientDet', linewidth=2)

plt.xlabel('Epochs', fontsize=12)
plt.ylabel('Training Loss', fontsize=12)
plt.title('Training Loss Comparison over 600 Epochs', fontsize=14)
plt.legend(fontsize=12)
plt.grid(True)
plt.tight_layout()
plt.show()
