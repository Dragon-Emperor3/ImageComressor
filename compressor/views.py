from django.shortcuts import render, redirect
from .forms import ImageUploadForm, ImageCompressForm, ImageDownloadForm
from django.conf import settings
import cv2
import os
from .helper import delete, print_file_size

# Create your views here.

def home(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.cleaned_data['image']
            compression_level= form.cleaned_data['compression_level']
            destination_folder = 'images/'  # Specify the destination folder within 'staticfiles'

            # Get the absolute path to the destination folder
            #destination_path = os.path.join(settings.STATICFILES_DIRS[0], destination_folder) # for static file in compressor
            destination_path = os.path.join(settings.STATIC_ROOT, destination_folder) # for deployment
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
            cv2.imwrite(destination_path+ "compressed.jpg", img, [cv2.IMWRITE_JPEG_QUALITY, compression_level])


            # Construct the URL for the uploaded file
            #image_url = os.path.join(settings.STATIC_URL, destination_folder, image.name) # for static files
            image_url = os.path.join(settings.STATIC_ROOT, destination_folder, image.name)  # for deployment
            print(image_url)
            context= {
                    'o_size': print_file_size(save_path), 
                    'c_size': print_file_size(destination_path+ "compressed.jpg"),
                    'image_name': image.name,
                }
            return render(request, 'compressor/show.html', context)   

        else:
            print(form.errors)  
    else:
        form = ImageUploadForm()       
    
        
    return render(request, 'compressor/index.html', {'form': form})


def show(request):
    if request.method == 'POST':
        form = ImageCompressForm(request.POST)
        if form.is_valid():
            compression_level= form.cleaned_data['compression_level']
            #destination_path = os.path.join(settings.STATICFILES_DIRS[0], 'images/')                         
            destination_path = os.path.join(settings.STATIC_ROOT, 'images/') # for deployment
            image_name= ''
            for file_name in os.listdir(destination_path):
                if 'compressed.jpg' in file_name:
                    continue
                image_name = file_name
                break
            save_path = os.path.join(destination_path, image_name)
            img= cv2.imread(save_path)
            # cv2.imread('lenna.jpg', img)
            cv2.imwrite(destination_path+ "compressed.jpg", img, [cv2.IMWRITE_JPEG_QUALITY, compression_level])

            #image_url = os.path.join(settings.STATIC_URL, 'images/', image_name)
            image_url = os.path.join(settings.STATIC_URL, 'images/', image_name) 
            print(image_url)
            context= {
                    'o_size': print_file_size(save_path), 
                    'c_size': print_file_size(destination_path+ "compressed.jpg"),
                    'image_name': image_name,
                }
            return render(request, 'compressor/show.html', context)            
    else:
        form = ImageCompressForm()
    return render(request, 'compressor/compress.html', {'form': form})


def download(request):
    if request.method == 'POST':
        form = ImageDownloadForm(request.POST)
        if form.is_valid():
            download_type= form.cleaned_data['download_type']
            #destination_path = os.path.join(settings.STATICFILES_DIRS[0], 'images/')
            destination_path = os.path.join(settings.STATIC_ROOT, 'images/') # for deployment
            img= cv2.imread(destination_path+ 'compressed.jpg')
            image_name= 'compressed.' + str(download_type)
            cv2.imwrite(destination_path + image_name, img)
            context= {'image_name': image_name}

            return render(request, 'compressor/download.html', context)

    else:
        form= ImageDownloadForm()
    return render(request, 'compressor/download.html', {'form': form})