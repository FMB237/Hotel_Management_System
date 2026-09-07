# This is the file we gonna used for making the file handlings in our project
# I means maining handling pictures uploads for our hostels
import os 
import uuid
from fastapi import UploadFile

# Let define our base directoty for uploads

UPLOAD_DIR = "uploads"

def save_upload_file(upload_file:UploadFile,folder:str)-> str:
    """let create our upload folder"""

    folder_path = os.path.join(UPLOAD_DIR,folder)
    os.makedirs(folder_path,exist_ok=True)

    """Let also check the unique names generations to prevent overwriting """
    file_extension = os.path.splitext(upload_file.filename)[1]
    unique_filename = f"{uuid.uuid4().hex}{file_extension}"

    """Define the full path"""
    file_path = os.path.join(folder_path,unique_filename)

    with open(file_path,"wb") as buffer:
        buffer.write(upload_file.file.read())
    
    # Return the relative path to save in the database
    return f"{folder}/{unique_filename}"