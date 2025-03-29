import os
from PIL import Image

def convert_images_to_webp(source_folder, destination_folder):
    """Converts all image files in a source folder (and subfolders) to WebP format and saves them in a destination folder."""
    supported_extensions = ('.png', '.jpg', '.jpeg', '.bmp', '.tiff')

    # Create destination folder if it doesn't exist
    os.makedirs(destination_folder, exist_ok=True)

    for root, _, files in os.walk(source_folder):
        for file in files:
            if file.lower().endswith(supported_extensions):
                file_path = os.path.join(root, file)

                # Preserve folder structure
                relative_path = os.path.relpath(root, source_folder)
                save_folder = os.path.join(destination_folder, relative_path)
                os.makedirs(save_folder, exist_ok=True)

                new_file_path = os.path.join(save_folder, os.path.splitext(file)[0] + ".webp")

                try:
                    with Image.open(file_path) as img:
                        img.save(new_file_path, "WEBP", quality=85)
                    print(f"Converted: {file_path} → {new_file_path}")
                except Exception as e:
                    print(f"Failed to convert {file_path}: {e}")

# Define source and destination folders
source_folder = "/Users/heysi/Desktop/company-website-assets-2/src"
destination_folder = "/Users/heysi/Desktop/company-website-assets-2/src/assets2"

convert_images_to_webp(source_folder, destination_folder)
