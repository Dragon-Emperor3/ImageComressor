import os
def print_file_size(file):

    File_Size = os.path.getsize(file)
    File_Size_MB = round(File_Size/1024/1024,2)
    if 0<File_Size_MB and File_Size_MB<1:
        return str(round(File_Size/1024,3)) + " KB" 
    else:
        return str(File_Size_MB) + " MB" 

def delete(images_folder):
    for filename in os.listdir(images_folder):
        file_path = os.path.join(images_folder, filename)
        if os.path.isfile(file_path):
            os.remove(file_path)