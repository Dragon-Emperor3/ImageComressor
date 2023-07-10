import os
def print_file_size(file_path):
    file_size = os.path.getsize(file_path)
    file_size_mb = round(file_size / (1024 * 1024), 2)
    
    if 0 < file_size_mb < 1:
        return f"{round(file_size / 1024, 3)} KB"
    else:
        return f"{file_size_mb} MB"

def delete(images_folder):
    for filename in os.listdir(images_folder):
        file_path = os.path.join(images_folder, filename)
        if os.path.isfile(file_path):
            os.remove(file_path)

def calculate_percentage(first, second):
    x= float(''.join(filter(str.isdigit, first + '.')))
    y= float(''.join(filter(str.isdigit, second + '.')))
    percentage_difference = ((y - x) / x) * 100
    if percentage_difference <0:
        return "<"+str(-1*round(percentage_difference,2))
    else:
        return ">"+str(round(percentage_difference,2))
