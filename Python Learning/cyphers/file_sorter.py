import os
import time
import shutil
from pathlib import Path
# Path.home() finds your user folder (e.g., C:/Users/Name), 
# and / "Downloads" adds the specific folder we want to organize.
target_dir = Path.home() / "Downloads"
#Dictionary for where we want to sort each file type and in what folder
file_map = {
    ".jpeg" : "Pictures",
    ".jpg"  : "Pictures",
    ".pdf"  : "Documents",
    ".mp4"  : "Videos",
    ".png"  : "Pictures",
    ".mov"  : "Videos",
    ".heic" : "Pictures",
    ".docx" : "Documents",
    ".mp3"  : "Audio",  
    ".m4a"  : "Audio",
    ".wav"  : "Audio",
    ".zip"  : "Archives",
    ".exe"  : "Archives",
    ".msi"  : "Archives",
    ".rar"  : "Archives.",
    ".pptx" : "Documents",
    ".xlsx" : "Documents",

}
def organize_folder ():
    
    for file in target_dir.iterdir(): 
        print("Scanning...")
        # .iterdir() allows us to loop through every item inside the target directory.
        if file.is_file():
        # Move only files

           extension = file.suffix.lower()
           # Get the extension (ending) of each file: .pdf, .jpg, etc.

           if extension in file_map:
             # If the extension is in our dictionary, start the move process.
             folder_name = file_map[extension]

             # Construct the full path for the destination (Downloads/FolderName).
             dest_path = target_dir / folder_name

             dest_path.mkdir(exist_ok=True)
             # Check if that folder exists, and if not, create it.
             # exist_ok = True  prevents an error if the folder is already there

             shutil.move(str(file), str(dest_path / file.name))
             # first argument is the source, the second is the destination folder
             print(f"Moved {file.name} to {folder_name}")


if __name__ == "__main__":
    while True:
       try:
          organize_folder()
       except Exception as e:
          print(f"Error: {e}")

       time.sleep(60)
          
          

            


        

