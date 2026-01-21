from post_generator import generate_post
from image_generator import generate_image
from auto_post import post_to_x
import os

os.makedirs("output", exist_ok=True)

# Generate post
post = generate_post()
with open("output/post.txt", "w") as f:
    f.write(post)

# Generate image
generate_image()

print("✅ New post and image generated!")
print("📄 output/post.txt")
print("🖼️ output/image.png")

# Optional auto post
post_to_x()
