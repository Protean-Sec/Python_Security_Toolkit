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
    ".rar"  : "Archives",
    ".pptx" : "Documents",
    ".xlsx" : "Documents",
    ".webp" : "Pictures"

}
def organize_folder ():
   print("Scanning...")
    # Check if any files were moved. Deafult is false because this is before the loop 
   moved_any = False 
   for file in target_dir.iterdir(): 
        
        # .iterdir() allows us to loop through every item inside the target directory,
        # In this case its downloads.
       if file.is_file():
        # If a file is in downloads
           extension = file.suffix.lower()
           # Get the extension (ending) of each file: .pdf, .jpg, etc.

           if extension in file_map:
             # If the extension is in our dictionary, start the move process.
             folder_name = file_map[extension]

             # Construct the full path for the destination (Downloads/FolderName)
             # In simple terms, moves file to its designated folder (example: jpg goes to Images).
             dest_path = target_dir / folder_name

             dest_path.mkdir(exist_ok=True)
             # Check if that folder exists, and if not, create it.
             # exist_ok = True  prevents an error if the folder is already there

             shutil.move(str(file), str(dest_path / file.name))
             # first argument is the source, the second is the destination folder
             print(f"Moved {file.name} to {folder_name}")

             moved_any = True

   if not moved_any:
     print("No files were found")


if __name__ == "__main__":
       try:
          organize_folder()
       except Exception as e:
          print(f"Error: {e}")

      