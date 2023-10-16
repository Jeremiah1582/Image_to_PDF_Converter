from PIL import Image #pip install pillow 
from os import listdir
import os
from dotenv import load_dotenv
load_dotenv()

output_dir= os.environ.get('CONVERTED_DIR')
source_dir = os.environ.get("IMG_DIR") #getting route from environment variable
comp_fileTypes = ('png', 'jpg', 'jpeg')

def convert_image_to_pdf():       
    for file in os.listdir(source_dir):
    #    check to see if file 
        if file.split('.')[-1] in comp_fileTypes:
            image = Image.open(source_dir + '/' + file)
            image_converted= image.convert('RGB')
            
            image_converted.save(
                os.path.join(
                    output_dir,
                    f'{file.split(".")[-2]}.pdf'))
        else:
            print('file was not convertible')

convert_image_to_pdf()