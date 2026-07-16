import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("apple.jpg")

if img is None:
    print("Image not found")
    exit()

rgb = np.zeros_like(img)

rgb[:, :, 0] = img[:, :, 2]  # R
rgb[:, :, 1] = img[:, :, 1]  # G
rgb[:, :, 2] = img[:, :, 0]  # B

rgb_norm = rgb.astype(np.float32) / 255.0

R = rgb_norm[:, :, 0]
G = rgb_norm[:, :, 1]
B = rgb_norm[:, :, 2]


gray = (0.299 * R + 0.587 * G + 0.114 * B)
gray = (gray * 255).astype(np.uint8)


H = np.zeros_like(R)
S = np.zeros_like(R)
V = np.zeros_like(R)

Cmax = np.maximum(np.maximum(R, G), B)
Cmin = np.minimum(np.minimum(R, G), B)

delta = Cmax - Cmin

# Hue
mask = delta != 0

mask_r = (Cmax == R) & mask
mask_g = (Cmax == G) & mask
mask_b = (Cmax == B) & mask

H[mask_r] = (60 * ((G[mask_r] - B[mask_r]) / delta[mask_r]) + 360) % 360
H[mask_g] = 60 * (((B[mask_g] - R[mask_g]) / delta[mask_g]) + 2)
H[mask_b] = 60 * (((R[mask_b] - G[mask_b]) / delta[mask_b]) + 4)


S[Cmax != 0] = delta[Cmax != 0] / Cmax[Cmax != 0]

V = Cmax

# Scale to display
HSV = np.zeros_like(rgb)

HSV[:, :, 0] = (H / 2).astype(np.uint8)
HSV[:, :, 1] = (S * 255).astype(np.uint8)
HSV[:, :, 2] = (V * 255).astype(np.uint8)


H2 = H.copy()

L = (Cmax + Cmin) / 2

S2 = np.zeros_like(R)

mask = delta != 0

S2[mask] = delta[mask] / (1 - np.abs(2 * L[mask] - 1))

HSL = np.zeros_like(rgb)

HSL[:, :, 0] = (H2 / 2).astype(np.uint8)
HSL[:, :, 1] = (S2 * 255).astype(np.uint8)
HSL[:, :, 2] = (L * 255).astype(np.uint8)

def inverse_gamma(c):
    return np.where(
        c > 0.04045,
        ((c + 0.055) / 1.055) ** 2.4,
        c / 12.92
    )

r = inverse_gamma(R)
g = inverse_gamma(G)
b = inverse_gamma(B)

X = r * 0.4124564 + g * 0.3575761 + b * 0.1804375
Y = r * 0.2126729 + g * 0.7151522 + b * 0.0721750
Z = r * 0.0193339 + g * 0.1191920 + b * 0.9503041

X /= 0.95047
Y /= 1.00000
Z /= 1.08883

def f(t):
    return np.where(
        t > 0.008856,
        np.cbrt(t),
        7.787 * t + 16 / 116
    )

fx = f(X)
fy = f(Y)
fz = f(Z)

L_lab = (116 * fy) - 16
A_lab = 500 * (fx - fy)
B_lab = 200 * (fy - fz)

LAB = np.zeros_like(rgb)

LAB[:, :, 0] = np.clip(L_lab * 255 / 100, 0, 255)
LAB[:, :, 1] = np.clip(A_lab + 128, 0, 255)
LAB[:, :, 2] = np.clip(B_lab + 128, 0, 255)

LAB = LAB.astype(np.uint8)

plt.figure(figsize=(15, 8))

plt.subplot(2,3,1)
plt.imshow(rgb)
plt.title("RGB")
plt.axis("off")

plt.subplot(2,3,2)
plt.imshow(HSV)
plt.title("HSV")
plt.axis("off")

plt.subplot(2,3,3)
plt.imshow(HSL)
plt.title("HSL")
plt.axis("off")

plt.subplot(2,3,4)
plt.imshow(LAB)
plt.title("LAB")
plt.axis("off")

plt.subplot(2,3,5)
plt.imshow(gray, cmap="gray")
plt.title("Grayscale")
plt.axis("off")

plt.tight_layout()
plt.show()