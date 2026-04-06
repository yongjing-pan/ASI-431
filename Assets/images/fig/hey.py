import os
from pathlib import Path

def rename_images_by_date(folder_path, extensions=None):
    # Default to common image extensions if none provided
    if extensions is None:
        extensions = {'.png', '.jpg', '.jpeg', '.gif', '.bmp', '.tiff'}
    
    # Path object for the directory
    directory = Path(folder_path)
    
    # 1. Gather all image files and their modification times
    image_files = []
    for file in directory.iterdir():
        if file.suffix.lower() in extensions:
            # Using st_mtime (last modification). Use st_ctime for creation time on Windows.
            image_files.append((file, file.stat().st_mtime))
    
    # 2. Sort files by the timestamp (ascending)
    image_files.sort(key=lambda x: x[1])
    
    # 3. Rename files sequentially
    print(f"Found {len(image_files)} images. Starting rename...")
    
    for index, (old_path, timestamp) in enumerate(image_files, start=1):
        new_name = f"{index}.png"
        new_path = directory / new_name
        
        # Check if the destination name already exists to avoid overwriting
        if new_path.exists() and old_path != new_path:
            print(f"Warning: {new_name} already exists. Skipping {old_path.name}")
            continue
            
        try:
            old_path.rename(new_path)
            print(f"Renamed: {old_path.name} -> {new_name}")
        except Exception as e:
            print(f"Error renaming {old_path.name}: {e}")

if __name__ == "__main__":
    # Replace '.' with your folder path if needed
    target_folder = "." 
    rename_images_by_date(target_folder)