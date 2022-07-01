import os
import shutil

from os import listdir
from os.path import isfile, join

def sort_files(path):

    files = [f for f in listdir(path) if isfile (join(path, f))]

    executable_ext = ['.exe', '.msi']
    image_ext = ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.svg']
    video_ext = ['.mp4', '.mkv', '.avi', '.mov', '.wmv', '.flv', '.mpg', '.mpeg']
    document_ext = ['.doc', '.docx', '.odt', '.xls', '.xlsx', '.ppt', '.pptx', '.pdf', '.txt', '.rtf']
    code_ext = ['.c', '.cpp', '.h', '.hpp', '.java', '.js', '.json', '.py', '.rb', '.sh', '.sql', '.xml', '.yml', '.html', '.html', '.css', '.scss', '.sass', '.less', '.cfm', '.cfml', '.ts', '.tsx', '.jsx', '.mod', '.go', '.rs']
    sound_ext = ['.aif', '.aiff', '.flac', '.mp3', '.ogg', '.wav']
    compressed_ext = ['.7z', '.zip', '.rar', '.tar', '.gz', '.bz2', '.xz', '.z', '.tar.gz', '.tar.bz2', '.tar.xz', '.tar.z', '.tar.7z']

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
    
    for i in files:
        if i.endswith(tuple(executable_ext)):
            src_path=path + '\\' + i
            dest_path=path + "\Executables"
            shutil.move(src_path, dest_path)
            print(f"\033[1;32;40m{src_path}\033[1;36;40m >>>\033[1;34;40m Executables")
        elif i.endswith(tuple(image_ext)):
            src_path=path + '\\' + i
            dest_path=path + "\Images"
            shutil.move(src_path, dest_path)
            print(f"\033[1;32;40m{src_path}\033[1;36;40m >>>\033[1;34;40m Images")
        elif i.endswith(tuple(video_ext)):
            src_path=path + '\\' + i
            dest_path=path + "\Videos"
            shutil.move(src_path, dest_path)
            print(f"\033[1;32;40m{src_path}\033[1;36;40m >>>\033[1;34;40m Videos")
        elif i.endswith(tuple(document_ext)):
            src_path=path + '\\' + i
            dest_path=path + "\Documents"
            shutil.move(src_path, dest_path)
            print(f"\033[1;32;40m{src_path}\033[1;36;40m >>>\033[1;34;40m Documents")
        elif i.endswith(tuple(code_ext)):
            src_path=path + '\\' + i
            dest_path=path + "\Code Files"
            shutil.move(src_path, dest_path)
            print(f"\033[1;32;40m{src_path}\033[1;36;40m >>>\033[1;34;40m Code Files")
        elif i.endswith(tuple(sound_ext)):
            src_path=path + '\\' + i
            dest_path=path + "\Sounds"
            shutil.move(src_path, dest_path)
            print(f"\033[1;32;40m{src_path}\033[1;36;40m >>>\033[1;34;40m Sounds")
        elif i.endswith(tuple(compressed_ext)):
            src_path=path + '\\' + i
            dest_path=path + "\Compressed Files"
            shutil.move(src_path, dest_path)
            print(f"\033[1;32;40m{src_path}\033[1;36;40m >>>\033[1;34;40m Compressed Files")
        else:
            src_path=path + '\\' + i
            dest_path=path + "\Others"
            shutil.move(src_path, dest_path)
            print(f"\033[1;32;40m{src_path}\033[1;36;40m >>>\033[1;34;40m Others")

if __name__ == "__main__":
    sort_files(r"PLEASE ENTER THE PATH OF THE FOLDER TO BE SORTED")
    print("\033[1;31;40m***********************************")
    print("\033[1;35;40mAll Files Moved to Their Destined Folder.")