# ВАЖНО фото не должны содержать русских символов ! Так же не стоит импортировать фото с рабочего стола
# IMPORTANT photos must not contain Russian characters ! Also, do not import photos from your desktop


import os
import pathlib
import shutil

import tensorflow.keras
from PIL import Image, ImageOps
import numpy as np






def ai(self):

    def manga():
        os.chdir(path)  # меняем деректорию
        os.mkdir(str(Class_Name[0]).strip('[]').strip("'"))  # Создаем папку в дерриктории path/
        shutil.copy2(path_photo, str(User_Path[0]).strip('[]').strip("'"))

    def Other():
        os.chdir(path)  # меняем деректорию
        os.mkdir(str(Class_Name[1]).strip('[]').strip("'"))
        shutil.copy2(path_photo, str(User_Path[1]).strip('[]').strip("'"))




    # Открытие и запись в фаил масива путей str (из main --> GetFileNames)
    # Opening and writing an array of str paths to a file from(main --> GetFileNames)
    filenames_1 = open('G:/SortPhoto1.1/code/data/getFileNames.txt', 'r')         # ВАЖНО  для работы прграммы укажите свой путь до текстового файла
    filenames = filenames_1.read()                                                # IMPORTANT for the program to work, specify your path to the text file
    filenames_final=(filenames.replace("'",'').replace(' ', '').split(','))
    # Открытие и запись в фаил масива путей str (из main --> GetDirectory)
    # Opening and writing an array of str paths to a file from(main --> GetFileNames)
    Your_Directory_1 = open('G:/SortPhoto1.1/code/data/getDirectory.txt', 'r')    # ВАЖНО  для работы прграммы укажите свой путь до текстового файла
    Your_Directory = Your_Directory_1.read()                                      # IMPORTANT for the program to work, specify your path to the text file

    # Код ai
    # ai code
    np.set_printoptions(suppress=True)
    model = tensorflow.keras.models.load_model('keras_model.h5')
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)





    # Цикл создан для того , что бы программа понимала сколько элементов
    # всего было выделено и столько же раз применяла ai
    # It does not matter
    for i in range (filenames.count(',')+1):

        # Код ai
        # ai code
        image = Image.open(filenames_final[i])
        size = (224, 224)
        image = ImageOps.fit(image, size, Image.ANTIALIAS)
        image_array = np.asarray(image)
        normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1
        data[0] = normalized_image_array
        prediction = model.predict(data)





        # Работа с данными для дальнешего использования
        # Working with data for future reference
        filenames_final_for_path = filenames_final[i][::-1] # переворот строки ; # flip the line
        prediction_medium = (str(prediction)[2:-2].split()) # шансы после ai в строке ; # odds after ai in the row
        file = (filenames_final_for_path[:filenames_final_for_path.find('/')][::-1])
        # Пути
        # Paths
        path_photo = filenames_final[i]     # Путь до фото + имя фото ; # Path to photo + photo name
        path = filenames_final[i].replace(file , '')[:-1]   # Путь до фто без имени фото ; # Path to photo without photo name
        # Масивы данных
        # Data arrays
        Values_AI = [float(prediction_medium[0]),float(prediction_medium[1])] # Manga, Other
        Class_Name = ['Manga', 'Other']  # Имя папки , которая создатся ; # Name of the folder that is being created
        User_Path = [path + '/' + Class_Name[0] , [path + '/' + Class_Name[1]]] # Путь пользователя +  Class_Name ; # User path + Class name



        # Проверка выбрал ли пользователь деррикторию кнопкой YourFolder
        # Check whether the user has selected the derrictory with the YourFolder button
        if Your_Directory != ' ' :
            path = Your_Directory
        else:
            path = path

        print(Values_AI)




        # Условия для ai , что и по каким папкам отправлять
        # Conditions for ai, what to send and to which folders
        # Manga
        if Values_AI[0] > Values_AI[1] :
            if os.path.exists(str(User_Path[0]).strip('[]').strip("'")) == False:  # Проверяем есть ли такой путь в дериктории ; # Check if there is such a path in the directory
                manga()
            else:
                os.chdir(path)
                shutil.copy2(path_photo, str(User_Path[0]).strip('[]').strip("'")) # Если
        # Other
        else:
            if os.path.exists(str(User_Path[1]).strip('[]').strip("'")) == False:
                Other()
            else:
                os.chdir(path)
                shutil.copy2(path_photo, str(User_Path[1]).strip('[]').strip("'"))

    with open("G:/SortPhoto1.1/code/data/getDirectory.txt", "w") as file:
        file.write(' ')