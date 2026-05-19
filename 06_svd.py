import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

img = Image.open("image.png").convert("L")

A = np.array(img, dtype=float)

U, S, VT = np.linalg.svd(A, full_matrices=False)

print("Shape of U:", U.shape)
print("Shape of S:", S.shape)
print("Shape of VT:", VT.shape)

A_reconstructed = U @ np.diag(S) @ VT

print("Reconstruction correct?:",
      np.allclose(A, A_reconstructed))


def compress_image(U, S, VT, k):
    U_k = U[:, :k]
    S_k = np.diag(S[:k])
    VT_k = VT[:k, :]

    A_k = U_k @ S_k @ VT_k

    return A_k

k_values = [5, 20, 50, 150]

compressed_images = []

for k in k_values:
    A_k = compress_image(U, S, VT, k)
    compressed_images.append(A_k)

plt.figure(figsize=(16, 8))

plt.subplot(1, 5, 1)
plt.imshow(A, cmap='gray')
plt.title("Original")
plt.axis("off")

for i, k in enumerate(k_values):
    plt.subplot(1, 5, i + 2)
    plt.imshow(compressed_images[i], cmap='gray')
    plt.title(f"k = {k}")
    plt.axis("off")

plt.tight_layout()
plt.show()