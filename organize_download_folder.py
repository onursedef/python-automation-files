import os
from pydoc import doc
import shutil

from os import listdir
from os.path import isfile, join

def sort_files(path):

    files = [f for f in listdir(path) if isfile (join(path, f))]
    exe_files = []
    img_files = []
    vid_files = []
    doc_files = []
    code_files = []
    comp_files = []
    sound_files = []
    others = []

    if os.path.isdir(f"{path}\Images") == False:
        os.mkdir(f"{path}\Images")
    elif os.path.isdir(f"{path}\Executables") == False:
        os.mkdir(f"{path}\Executables")
    elif os.path.isdir(f"{path}\Videos") == False:
        os.mkdir(f"{path}\Videos")
    elif os.path.isdir(f"{path}\Documents" == False):
        os.mkdir(f"{path}\Documents")
    elif os.path.isdir(f"{path}\Compressed Files") == False:
        os.mkdir(f"{path}\Compressed Files")
    elif os.path.isdir(f"{path}\Sounds") == False:
        os.mkdir(f"{path}\Sounds")
    elif os.path.isdir(f"{path}\Code Files") == False:
        os.mkdir(f"{path}\Code Files")
    elif os.path.isdir(f"{path}\Others") == False:
        os.mkdir(f"{path}\Others")
    
    
    for f in files:
        if f.endswith(".png") | f.endswith(".jpeg") | f.endswith(".jpg") | f.endswith(".gif") | f.endswith(".bmp") | f.endswith(".tiff") | f.endswith(".webp") | f.endswith(".svg"):
            img_files.append(f)
        elif f.endswith(".exe") | f.endswith(".msi"):
            exe_files.append(f)
        elif f.endswith(".mov") | f.endswith(".mp4") | f.endswith(".wmv") | f.endswith(".avi") | f.endswith(".flv") | f.endswith(".webm") | f.endswith(".mkv"):
            vid_files.append(f)
        elif f.endswith(".docx") | f.endswith(".doc") | f.endswith(".pdf") | f.endswith(".odt") | f.endswith(".xls") | f.endswith(".xlsx") | f.endswith(".ppt") | f.endswith(".pptx") | f.endswith(".txt"):
            doc_files.append(f)
        elif f.endswith(".py") | f.endswith(".ipynb") | f.endswith(".js") | f.endswith(".json") | f.endswith(".java") | f.endswith(".html") | f.endswith(".htm") | f.endswith(".cfm") | f.endswith(".cfml") | f.endswith(".css") | f.endswith(".sass") | f.endswith(".scss") | f.endswith(".jsx") | f.endswith(".ts") | f.endswith(".tsx"):
            code_files.append(f)
        elif f.endswith(".7z") | f.endswith(".arj") | f.endswith(".rar") | f.endswith(".zip") | f.endswith(".tar.gz") | f.endswith(".tar.xz"):
            comp_files.append(f)
        elif f.endswith(".aif") | f.endswith(".cda") | f.endswith(".mid") | f.endswith(".midi") | f.endswith(".mp3") | f.endswith(".mpa") | f.endswith(".ogg") | f.endswith(".wav") | f.endswith(".wma") | f.endswith(".wpl"):
            sound_files.append(f)
        else:
            others.append(f)
        
    for file in exe_files:
        src_path=path + '\\' + file
        dest_path=path + "\Executables"
        shutil.move(src_path, dest_path)
        print(f"\033[1;32;40m{src_path}\033[1;36;40m >>>\033[1;34;40m Executables")
    for file in img_files:
        src_path=path + '\\' + file
        dest_path=path + "\Images"
        shutil.move(src_path, dest_path)
        print(f"\033[1;32;40m{src_path}\033[1;36;40m >>>\033[1;34;40m Images")
    for file in vid_files:
        src_path=path + '\\' + file
        dest_path=path + "\Videos"
        shutil.move(src_path, dest_path)
        print(f"\033[1;32;40m{src_path}\033[1;36;40m >>>\033[1;34;40m Videos")
    for file in doc_files:
        src_path=path + '\\' + file
        dest_path=path + "\Documents"
        shutil.move(src_path, dest_path)
        print(f"\033[1;32;40m{src_path}\033[1;36;40m >>>\033[1;34;40m Documents")
    for file in code_files:
        src_path=path + '\\' + file
        dest_path=path + r"\Code Files"
        shutil.move(src_path, dest_path)
        print(f"\033[1;32;40m{src_path}\033[1;36;40m >>>\033[1;34;40m Code Files")
    for file in comp_files:
        src_path=path + '\\' + file
        dest_path=path + r"\Compressed Files"
        shutil.move(src_path, dest_path)
        print(f"\033[1;32;40m{src_path}\033[1;36;40m >>>\033[1;34;40m Compressed Files")
    for file in sound_files:
        src_path=path + '\\' + file
        dest_path=path + "\Sounds"
        shutil.move(src_path, dest_path)
        print(f"\033[1;32;40m{src_path}\033[1;36;40m >>>\033[1;34;40m Sounds")
    for file in others:
        src_path=path + '\\' + file
        dest_path=path + "\Others"
        shutil.move(src_path, dest_path)
        print(f"\033[1;32;40m{src_path}\033[1;36;40m >>>\033[1;34;40m Others")
    

if __name__ == "__main__":
    sort_files(r"PLEASE ENTER YOUR PATH TO DOWNLOAD FOLDER")
    print("\033[1;31;40m***********************************")
    print("\033[1;35;40mAll Files Moved to Their Destined Folder.")