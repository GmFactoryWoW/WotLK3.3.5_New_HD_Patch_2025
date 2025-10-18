import os
from PIL import Image

# Taille maximale
MAX_SIZE = (512, 512)  # max width/height

def process_image(path):
    img = Image.open(path).convert("RGBA")

    # Resize seulement si trop grand
    if img.width > MAX_SIZE[0] or img.height > MAX_SIZE[1]:
        img.thumbnail(MAX_SIZE, Image.LANCZOS)

    # Sauvegarde par-dessus l'original sans créer de canvas
    img.save(path, "PNG")
    print(f"✅ Overwritten: {path}")

def main():
    for file in os.listdir("."):
        if file.lower().endswith(".png"):
            process_image(file)

if __name__ == "__main__":
    main()
