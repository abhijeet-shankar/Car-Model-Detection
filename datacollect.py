from pygoogle_image import image as meow
cars=['mercedes','toyota','ferrari','tesla','volkswagen','bugatti','rolls royce','maserati']
try:
    for i in range (len(cars)):
        meow.download(cars[i], limit= 3)
        print("Images of "+cars[i]+" downloaded successfully")    
except:
    print("Error downloading files")    