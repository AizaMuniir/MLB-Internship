import cv2
import numpy as np
import matplotlib.pyplot as plt


img = cv2.imread("apple.jpg")

if img is None:
    print("Image not found!")
    exit()


rgb = img[:, :, ::-1]

rgb = rgb.astype(float) / 255.0

R = rgb[:, :, 0]
G = rgb[:, :, 1]
B = rgb[:, :, 2]


def gamma_correct(value):
    return np.where(
        value > 0.04045,
        ((value + 0.055) / 1.055) ** 2.4,
        value / 12.92
    )


R = gamma_correct(R)
G = gamma_correct(G)
B = gamma_correct(B)


X = R * 0.4124 + G * 0.3576 + B * 0.1805
Y = R * 0.2126 + G * 0.7152 + B * 0.0722
Z = R * 0.0193 + G * 0.1192 + B * 0.9505


X = X / 0.95047
Y = Y / 1.00000
Z = Z / 1.08883


def f(t):
    return np.where(
        t > 0.008856,
        np.cbrt(t),
        (7.787 * t) + (16 / 116)
    )


fx = f(X)
fy = f(Y)
fz = f(Z)


L = (116 * fy) - 16
A = 500 * (fx - fy)
B_lab = 200 * (fy - fz)


L_display = np.clip(L * 255 / 100, 0, 255).astype(np.uint8)

A_display = np.clip(A + 128, 0, 255).astype(np.uint8)

B_display = np.clip(B_lab + 128, 0, 255).astype(np.uint8)


height, width = L_display.shape


L_channel = np.zeros((height, width), dtype=np.uint8)
A_channel = np.zeros((height, width), dtype=np.uint8)
B_channel = np.zeros((height, width), dtype=np.uint8)


for i in range(height):
    for j in range(width):
        L_channel[i][j] = L_display[i][j]
        A_channel[i][j] = A_display[i][j]
        B_channel[i][j] = B_display[i][j]


plt.figure(figsize=(12,8))

plt.subplot(2,2,1)
plt.imshow(rgb)
plt.title("Original RGB Image")
plt.axis("off")

plt.subplot(2,2,2)
plt.imshow(L_channel, cmap="gray")
plt.title("L Channel")
plt.axis("off")

plt.subplot(2,2,3)
plt.imshow(A_channel, cmap="gray")
plt.title("A Channel")
plt.axis("off")

plt.subplot(2,2,4)
plt.imshow(B_channel, cmap="gray")
plt.title("B Channel")
plt.axis("off")

plt.tight_layout()
plt.show()