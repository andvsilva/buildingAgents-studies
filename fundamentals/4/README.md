# 4. Deep Learning

# Neural Network Architecture: Explanation & Hands-On Examples

This repository provides a **conceptual and practical introduction to neural network architecture**, focusing on **layers, weights, and activation functions**.
The goal is to build intuition while also showing how these ideas translate into real code using **PyTorch**.

---

## 📌 What is a Neural Network Architecture?

A neural network is composed of **stacked layers** that transform inputs into outputs through learnable parameters.

Each layer performs the operation:

$$
\text{output} = \text{activation}(W \cdot x + b)
$$

Where:

* **x** → input vector
* **W** → weight matrix (learned during training)
* **b** → bias vector
* **activation** → non-linear function

Without activation functions, a neural network reduces to a linear model.

---

## 🧱 Layers

### 1. Input Layer

* Receives raw features
* No computation is performed
* Example: 10 input features → input dimension = 10

### 2. Hidden Layers

* Perform feature transformation
* Responsible for learning representations
* Common types:

  * Fully Connected (Dense / Linear)
  * Convolutional
  * Recurrent
  * Attention-based

This repository focuses on **fully connected layers**.

### 3. Output Layer

Depends on the task:

* **Regression** → 1 neuron, linear activation
* **Binary classification** → 1 neuron + sigmoid
* **Multi-class classification** → N neurons + softmax

---

## ⚙️ Weights and Biases

Each neuron computes:

$$
z = w_1x_1 + w_2x_2 + \dots + w_nx_n + b
$$

* **Weights** determine the importance of each input
* **Bias** shifts the activation threshold
* Both are optimized using **gradient descent**

---

## 🔥 Activation Functions

Activation functions introduce **non-linearity**, enabling neural networks to model complex patterns.

Common choices:

* **ReLU**: `max(0, x)` → default for hidden layers
* **Sigmoid**: outputs values in (0, 1)
* **Tanh**: outputs values in (−1, 1)
* **Softmax**: converts outputs into class probabilities

---

## 🧪 Hands-On Example (PyTorch)

### Define a Simple Neural Network

```python
import torch
import torch.nn as nn

class SimpleNN(nn.Module):
    def __init__(self, input_dim):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(input_dim, 16),
            nn.ReLU(),
            nn.Linear(16, 8),
            nn.ReLU(),
            nn.Linear(8, 1)
        )

    def forward(self, x):
        return self.net(x)

model = SimpleNN(input_dim=10)
print(model)
```

**Architecture overview:**

* Input layer: 10 features
* Hidden layer 1: 16 neurons
* Hidden layer 2: 8 neurons
* Output layer: 1 neuron

---

## 🔍 Inspecting Weights

```python
for name, param in model.named_parameters():
    print(name, param.shape)
```

Example output:

```
net.0.weight  torch.Size([16, 10])
net.0.bias    torch.Size([16])
```

This confirms the matrix multiplication:
[
W_{16 \times 10} \cdot x_{10} + b_{16}
]

---

## ▶️ Forward Pass Example

```python
x = torch.randn(5, 10)  # batch of 5 samples
y = model(x)
print(y.shape)
```

Output:

```
torch.Size([5, 1])
```

Each row corresponds to one prediction.

---

## 🧠 Intuition Behind the Architecture

* **Layers** → levels of abstraction
* **Weights** → control signal strength
* **Activations** → decision gates

Early layers learn simple patterns.
Deeper layers combine them into higher-level representations.

---

## 🌍 Real-World Applications

### Regression

* Predicting house prices
* Estimating energy consumption

### Classification

* Spam detection
* Sentiment analysis

The same architectural principles apply — only the data and loss function change.

---

## ⚠️ Common Mistakes

* Using too many layers with small datasets
* Forgetting activation functions
* Incorrect output activation for the task
* Skipping input normalization

---

## 🚀 Next Steps

Possible extensions:

* Training loop (loss + optimizer)
* Backpropagation math
* Activation visualization
* Architecture tuning
* CNNs and Transformers

---

## 🛠️ Requirements

* Python 3.9+
* PyTorch

---

## 📄 License

This project is intended for **educational purposes**.

---

Backpropagation computes gradients of the loss with respect to each parameter, and gradient descent uses those gradients to update the weights.

Below is a **didactic explanation + hands-on example**, written in the same style as a README section, focused on **understanding first, code second**.

---

# Backpropagation and Gradient Descent

**Explanation and Example**

This section explains how neural networks **learn**.
Learning happens in two tightly connected steps:

1. **Backpropagation** → computes gradients
2. **Gradient Descent** → updates parameters using those gradients

Together, they allow the network to improve its predictions.

---

## 1. The Learning Problem

A neural network makes predictions (\hat{y}) from inputs (x).
To measure how good those predictions are, we define a **loss function**:

$$
\mathcal{L}(y, \hat{y})
$$

* (y): true target
* ($\hat{y}$): model prediction

**Goal:** adjust the weights and biases so that the loss is minimized.

---

## 2. Gradient Descent: How Parameters Are Updated

Gradient descent is an optimization algorithm that updates parameters in the direction that **reduces the loss**.

For a parameter (w):

$$
w \leftarrow w - \eta \frac{\partial \mathcal{L}}{\partial w}
$$

Where:

* ($\eta$) is the **learning rate**
* ($\frac{\partial \mathcal{L}}{\partial w}$) is the **gradient**

### Intuition

* The gradient tells us **how the loss changes** when a parameter changes
* Gradient descent moves parameters **downhill** on the loss surface

---

## 3. Why Backpropagation Is Needed

A neural network has **many layers**, so the loss depends on parameters indirectly.

Example:
$$
\mathcal{L} \rightarrow y \rightarrow z_2 \rightarrow z_1 \rightarrow W_1
$$

To compute gradients efficiently, we use **backpropagation**, which applies the **chain rule** of calculus layer by layer, from the output back to the input.

---

## 4. Backpropagation: Core Idea

Backpropagation computes:

$$
\frac{\partial \mathcal{L}}{\partial W^{(l)}}
\quad \text{and} \quad
\frac{\partial \mathcal{L}}{\partial b^{(l)}}
$$

for **every layer (l)** in the network.

### Key idea:

* Errors are propagated **backward**
* Each layer receives information about how much it contributed to the final error

---

## 5. One Training Step (Conceptual View)

A single training step consists of:

1. **Forward pass**
   Input → layers → prediction
2. **Loss computation**
   Compare prediction with target
3. **Backward pass (backpropagation)**
   Compute gradients of loss w.r.t. parameters
4. **Parameter update (gradient descent)**
   Update weights and biases

---

## 6. Mathematical Snapshot (Simple Case)

For one neuron:

$$
z = Wx + b
$$

$$
\hat{y} = f(z)
$$

$$
\mathcal{L} = (y - \hat{y})^2
$$

Using the chain rule:

$$
\frac{\partial \mathcal{L}}{\partial W}
=\frac{\partial \mathcal{L}}{\partial \hat{y}}
\cdot\frac{\partial \hat{y}}{\partial z}
\cdot\frac{\partial z}{\partial W}
$$

Backpropagation automates this process for deep networks.

---

## 7. Example: Backpropagation in PyTorch

In PyTorch, **autograd** computes gradients automatically.

### Define a simple model

```python
import torch
import torch.nn as nn

model = nn.Linear(1, 1)  # y = Wx + b
criterion = nn.MSELoss()
optimizer = torch.optim.SGD(model.parameters(), lr=0.1)
```

---

### Forward pass and loss

```python
x = torch.tensor([[1.0], [2.0], [3.0]])
y = torch.tensor([[2.0], [4.0], [6.0]])

y_pred = model(x)
loss = criterion(y_pred, y)
```

---

### Backward pass (backpropagation)

```python
optimizer.zero_grad()  # clear old gradients
loss.backward()        # compute gradients
```

After this step:

* `model.weight.grad` contains (\frac{\partial \mathcal{L}}{\partial W})
* `model.bias.grad` contains (\frac{\partial \mathcal{L}}{\partial b})

---

### Gradient descent step

```python
optimizer.step()
```

This updates:

$$
W \leftarrow W - \eta \nabla_W \mathcal{L}
$$

---

## 8. Inspecting Gradients

```python
print(model.weight.grad)
print(model.bias.grad)
```

Gradients tell:

* Direction of steepest increase in loss
* How strongly each parameter affects the loss

---

## 9. Intuition Summary

* **Backpropagation** answers:
  *“How much did each parameter contribute to the error?”*
* **Gradient descent** answers:
  *“How should parameters change to reduce the error?”*

Together, they are the engine of neural network learning.

---

## 10. Common Pitfalls

* Learning rate too high → divergence
* Learning rate too low → very slow training
* Forgetting to zero gradients
* Vanishing or exploding gradients in deep networks

---

# Convolutional Neural Networks (CNNs) for Image Processing

CNNs are the **standard architecture for image tasks** like classification, object detection, and segmentation.
They exploit the **spatial structure of images**, reducing the number of parameters compared to fully connected networks.

---

## 1. Key Concepts

### 1.1 Convolutional Layer

* Performs **feature extraction** using learnable **filters (kernels)**.
* Each filter slides over the input image and computes a **dot product**, producing a **feature map**.
* Detects patterns like edges, textures, shapes.

Mathematical view:

$$
\text{FeatureMap}[i,j] = \sum_{m,n} \text{Input}[i+m,j+n] \cdot \text{Kernel}[m,n]
$$

---

### 1.2 Activation Function

* Non-linearity applied after convolution (usually **ReLU**).
* Example:

```python
x = tf.nn.relu(conv_output)
```

---

### 1.3 Pooling Layer

* Reduces spatial dimensions (**downsampling**) while keeping important features.
* Common types:

  * Max Pooling → keeps the maximum value in a window
  * Average Pooling → takes the average
* Example: 2x2 max pooling halves height and width.

---

### 1.4 Fully Connected / Dense Layers

* After convolution + pooling, flatten the feature maps and pass through fully connected layers.
* These layers perform **high-level reasoning**.
* Final layer depends on task:

  * **Classification** → softmax
  * **Binary classification** → sigmoid
  * **Regression** → linear

---

### 1.5 Dropout & Batch Normalization

* Dropout → prevent overfitting by randomly dropping neurons
* BatchNorm → normalize activations per batch for stability and faster convergence

---

## 2. Example: CNN for MNIST Digit Classification

```python
import tensorflow as tf
from tensorflow.keras import layers, models, datasets

# Load dataset
(x_train, y_train), (x_test, y_test) = datasets.mnist.load_data()
x_train, x_test = x_train[..., None]/255.0, x_test[..., None]/255.0  # normalize & add channel

# Build CNN
model = models.Sequential([
    layers.Conv2D(32, (3,3), activation='relu', input_shape=(28,28,1)),
    layers.MaxPooling2D((2,2)),
    layers.BatchNormalization(),

    layers.Conv2D(64, (3,3), activation='relu'),
    layers.MaxPooling2D((2,2)),
    layers.BatchNormalization(),

    layers.Flatten(),
    layers.Dense(128, activation='relu'),
    layers.Dropout(0.3),
    layers.Dense(10, activation='softmax')  # 10 classes
])

# Compile
model.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)

# Train
model.fit(x_train, y_train, epochs=5, batch_size=64, validation_split=0.1)

# Evaluate
test_loss, test_acc = model.evaluate(x_test, y_test)
print("Test accuracy:", test_acc)
```

---

## 3. Layer-by-layer intuition

| Layer          | Output   | Role                                |
| -------------- | -------- | ----------------------------------- |
| Conv2D 32x3x3  | 28x28x32 | Extracts low-level features (edges) |
| MaxPooling 2x2 | 14x14x32 | Downsample, reduce computation      |
| Conv2D 64x3x3  | 12x12x64 | Higher-level features               |
| MaxPooling 2x2 | 6x6x64   | Reduce spatial size                 |
| Flatten        | 2304     | Prepare for dense layers            |
| Dense 128      | 128      | High-level reasoning                |
| Dense 10       | 10       | Class probabilities                 |

---

## 4. Key Notes

* Convolutions **reuse weights** → fewer parameters than fully connected networks.
* Pooling layers help **generalization** and reduce computation.
* BatchNorm + Dropout help **stability and overfitting**.
* CNNs can be extended to:

  * Color images: input shape `(H, W, 3)`
  * Multi-class tasks: softmax with N outputs
  * Object detection: YOLO, Faster R-CNN
  * Segmentation: U-Net, DeepLab

---
