#the code that automates my file organizer
#watchdog library has not yet been implemented, so when I download something, it doesn not automatically move to its respected files.

import os
import shutil

file_path = '/Users/yuan/Downloads'

#transfer paths
pdf_path = '/Users/yuan/Downloads/PDFs'
text_path = '/Users/yuan/Downloads/TextFiles'
videos_path = '/Users/yuan/Videos'
presentations_path = '/Users/yuan/Downloads/Presentations'
word_Downloads_path = '/Users/yuan/Downloads/WordDocuments'
music_path = '/Users/Downloads/yuan/Music'
images_path = '/Users/yuan/Downloads/Pictures'
application_path = '/Users/yuan/Downloads/Applications'
zip_path = '/Users/yuan/Downloads/Archives'

#file types
pdf_extensions = [".pdf"]
text_extensions = [".txt"]
video_extensions = [".mp4", ".mov"]
presentations_extensions = [".ppt", ".pptx"]
word_extensions = [".doc", ".docx"]
music_extensions = [".mp3", ".mav"]
images_extensions = [".jpg", ".jpeg", ".png"]
application_extensions = [".app"]
zip_extensions = [".zip", ".rar", ".dmg", ".textClipping"]

def move_file(src_path, dst_path):
    try:
        shutil.move(src_path, dst_path)
        print(f"moved {src_path} to {dst_path}")
    except Exception as e:
        print(f"failed to move {src_path} to {dst_path}")

with os.scandir(file_path) as obj:
    for file in obj:
        if file.is_file():
            file_ext = '.'+((file.name).split("."))[1]
            
            if file_ext in pdf_extensions:
                move_file(file.path, pdf_path)

            if file_ext in text_extensions:
                move_file(file.path, text_path)

            if file_ext in video_extensions:
                move_file(file.path, videos_path)

            if file_ext in presentations_extensions:
                move_file(file.path, presentations_path)

            if file_ext in word_extensions:
                move_file(file.path, word_Downloads_path)

            if file_ext in music_extensions:
                move_file(file.path, music_path)

            if file_ext in images_extensions:
                move_file(file.path, images_path)

            if file_ext in application_extensions:
                move_file(file.path, application_path)

            if file_ext in zip_extensions:
                move_file(file.path, zip_path)
            
            else:
                move_file(file.path , zip_path)
            

