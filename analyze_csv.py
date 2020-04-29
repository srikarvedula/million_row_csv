import threading
from create_csv import *
from statistics import stdev
new_list=[]
new_list_2=[]
new_list_3=[]
new_list_4=[]
new_list_5=[]
def read_csv():
    with open(file_1) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        global new_list
        new_list = []
        for row in csv_reader:
            al=int(row[0])
            new_list.append(al)
    return new_list

def read_csv_2():
    with open(file_2) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        global new_list_2
        new_list_2 = []
        for row in csv_reader:
            al=int(row[0])
            new_list_2.append(al)
    return new_list_2

def read_csv_3():
    with open(file_3) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        global new_list_3
        new_list_3 = []
        for row in csv_reader:
            al=int(row[0])
            new_list_3.append(al)
    return new_list_3

def read_csv_4():
    with open(file_4) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        global new_list_4
        new_list_4 = []
        for row in csv_reader:
            al=int(row[0])
            new_list_4.append(al)
    return new_list_4

def read_csv_5():
    with open(file_5) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        global new_list_5
        new_list_5=[]
        for row in csv_reader:
            al=int(row[0])
            new_list_5.append(al)


t1=Thread(target=read_csv)
t2=Thread(target=read_csv_2)
t3=Thread(target=read_csv_3)
t4=Thread(target=read_csv_4)
t5=Thread(target=read_csv_5)

t1.start()
t2.start()
t3.start()
t4.start()
t5.start()

read_csv()
read_csv_2()
read_csv_3()
read_csv_4()
read_csv_5()


res_list=new_list+new_list_2+new_list_3+new_list_4+new_list_5
SD=stdev(res_list)
print("length of res list", len(res_list))
print("Standard Deviation: ",SD)
