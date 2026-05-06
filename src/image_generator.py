from PIL import Image
import numpy as np

# 1️⃣ Create a grayscale cover image (256x256)
cover_array = np.full((256, 256), 128, dtype=np.uint8)  # uniform gray image
cover_img = Image.fromarray(cover_array)
cover_img.save("cover.png")  # saves as cover.png

# 2️⃣ Create a binary secret image (64x64)
# Simple checkerboard pattern
secret_array = np.indices((64, 64)).sum(axis=0) % 2
secret_img = Image.fromarray(secret_array.astype(np.uint8) * 255)
secret_img.save("secret.png")  # saves as secret.png

print("✅ Example images created: cover.png and secret.png")
