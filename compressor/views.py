from django.shortcuts import render
from .forms import ImageUploadForm
from django.conf import settings
import cv2
import os


# Create your views here.
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


def compress_image(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.cleaned_data['image']
            destination_folder = 'images/'  # Specify the destination folder within 'staticfiles'

            # Get the absolute path to the destination folder
            destination_path = os.path.join(settings.STATICFILES_DIRS[0], destination_folder) # for static file in compressor
            #destination_path = os.path.join(settings.STATIC_ROOT, destination_folder) # for deployment
            delete(destination_path)
            # Create the destination folder if it doesn't exist
            os.makedirs(destination_path, exist_ok=True)

            # Save the uploaded file to the destination folder
            save_path = os.path.join(destination_path, image.name)
            with open(save_path, 'wb') as f:
                for chunk in image.chunks():
                    f.write(chunk)

            img= cv2.imread(save_path)
            # cv2.imread('lenna.jpg', img)
            cv2.imwrite(destination_path+ "compressed.jpg", img, [cv2.IMWRITE_JPEG_QUALITY, 30])



            # Construct the URL for the uploaded file
            image_url = os.path.join(settings.STATIC_URL, destination_folder, image.name) # for static files
            #image_url = os.path.join(settings.STATIC_ROOT, destination_folder, image.name)
            print(image_url)
            return render(request, 'compressor/show.html', )
    else:
        form = ImageUploadForm()
    return render(request, 'compressor/index.html', {'form': form})
