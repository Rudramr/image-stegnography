from PIL import Image

# Cover image
cover = Image.open("cover.png").convert("L")   # grayscale
cover = cover.resize((256, 256))
cover.save("cover1.png")

# Secret image
secret = Image.open("rudra.jpg").convert("1") # binary
secret = secret.resize((64, 64))
secret.save("secret1.png")

print("✅ Cover and Secret images are ready!")