#Написать функцию, которая принимает путь к директории с 
#изображениями и список расширений (.png, .jpg, .ico и 
#т.д.) и создает директории по полученному пути с наименованием 
#расширения, в которые записывает конвертированные исходные изображения по полученным форматам. 
import os
from PIL import Image

def convert_images(directory, extensions):
    files = os.listdir(directory)
    for file in files:
        filename, file_extension = os.path.splitext(file)
        if file_extension in extensions:
            source_path = os.path.join(directory, file)
            output_directory = os.path.join(directory, file_extension[1:])
            os.makedirs(output_directory, exist_ok=True)           
            output_path = os.path.join(output_directory, file)            
            image = Image.open(source_path)
            image.save(output_path)
            print("Конвертировано изображение {file} в директорию {output_directory}")
convert_images(directory, extensions)
