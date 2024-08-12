import os
import shutil
import sys
from datetime import datetime

def backup_files(source_dir, dest_dir):
    # Check if the source directory exists
    if not os.path.exists(source_dir):
        print(f"Error: Source directory '{source_dir}' does not exist.")
        return
    
    # Check if the destination directory exists, create it if not
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)
        print(f"Created destination directory '{dest_dir}'")

    # Loop through all files in the source directory
    for file_name in os.listdir(source_dir):
        source_file = os.path.join(source_dir, file_name)
        
        # Check if it is a file (not a directory)
        if os.path.isfile(source_file):
            dest_file = os.path.join(dest_dir, file_name)
            
            # If the destination file exists, append a timestamp to the filename
            if os.path.exists(dest_file):
                timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
                file_name, file_ext = os.path.splitext(file_name)
                dest_file = os.path.join(dest_dir, f"{file_name}_{timestamp}{file_ext}")
            
            # Attempt to copy the file to the destination
            try:
                shutil.copy2(source_file, dest_file)
                print(f"Copied '{source_file}' to '{dest_file}'")
            except Exception as e:
                print(f"Error copying '{source_file}': {e}")

if __name__ == "__main__":
    # Check for correct number of command-line arguments
    if len(sys.argv) != 3:
        print("Usage: python backup.py /path/to/source /path/to/destination")
    else:
        source_directory = sys.argv[1]
        destination_directory = sys.argv[2]
        backup_files(source_directory, destination_directory)