import zipfile
from create_csv import *

my_zip_1= zipfile.ZipFile('file_1.zip','w')
my_zip_1.write(file_1)
my_zip_1.close()

my_zip_2= zipfile.ZipFile('file_2.zip','w')
my_zip_2.write(file_2)
my_zip_2.close()

my_zip_3= zipfile.ZipFile('file_3.zip','w')
my_zip_3.write(file_3)
my_zip_3.close()

my_zip_4= zipfile.ZipFile('file_4.zip','w')
my_zip_4.write(file_4)
my_zip_4.close()

my_zip_5= zipfile.ZipFile('file_5.zip','w')
my_zip_5.write(file_5)
my_zip_5.close()