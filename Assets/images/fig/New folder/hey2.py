import os
from pathlib import Path

def rename_images_by_name(folder_path, extensions=None, start_index=1):
    # Default image extensions
    if extensions is None:
        extensions = {'.png', '.jpg', '.jpeg', '.gif', '.bmp', '.tiff'}

    directory = Path(folder_path)

    # 1. Gather image files
    image_files = [
        file for file in directory.iterdir()
        if file.is_file() and file.suffix.lower() in extensions
    ]

    # 2. Sort files by name (case-insensitive)
    image_files.sort(key=lambda f: f.name.lower())

    print(f"Found {len(image_files)} images. Starting rename...")

    # 3. First pass: rename to temporary names to avoid conflicts
    temp_files = []
    for i, old_path in enumerate(image_files):
        temp_path = directory / f"__temp_{i}{old_path.suffix}"
        old_path.rename(temp_path)
        temp_files.append(temp_path)

    # 4. Second pass: rename to final names
    for index, temp_path in enumerate(temp_files, start=start_index):
        new_name = f"{index}{temp_path.suffix}"
        new_path = directory / new_name

        try:
            temp_path.rename(new_path)
            print(f"Renamed: {temp_path.name} -> {new_name}")
        except Exception as e:
            print(f"Error renaming {temp_path.name}: {e}")

if __name__ == "__main__":
    target_folder = "."  # Change if needed
    rename_images_by_name(target_folder, start_index=15)