import csv
import random
import decimal
import string
import datetime
from threading import Thread
a=1000000
N=10
file_1='data.csv'
file_2='data_2.csv'
file_3='data_3.csv'
file_4='data_4.csv'
file_5='data_5.csv'
def create_csv():
    with open(file_1, 'w', newline="") as csvfile:
        start_date = datetime.date(2020, 1, 1)
        end_date = datetime.date(2020, 2, 1)
        time_between_dates = end_date - start_date
        days_between_dates = time_between_dates.days
        for _ in range(a):
            value = random.randint(0, 100)
            val_dec=decimal.Decimal(random.randrange(1, 99999))/100
            res_str = ''.join(random.choices(string.ascii_uppercase + string.digits, k=N))
            random_number_of_days = random.randrange(days_between_dates)
            random_date = start_date + datetime.timedelta(days=random_number_of_days)
            spamwriter = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            spamwriter.writerow([value,val_dec,res_str,random_date,res_str,random_date,value,val_dec])
def create_csv_2():
    with open(file_2, 'w', newline="") as csvfile:
        start_date = datetime.date(2020, 1, 1)
        end_date = datetime.date(2020, 2, 1)
        time_between_dates = end_date - start_date
        days_between_dates = time_between_dates.days
        for _ in range(a):
            value = random.randint(0, 100)
            val_dec=decimal.Decimal(random.randrange(1, 99999))/100
            res_str = ''.join(random.choices(string.ascii_uppercase + string.digits, k=N))
            random_number_of_days = random.randrange(days_between_dates)
            random_date = start_date + datetime.timedelta(days=random_number_of_days)
            spamwriter = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            spamwriter.writerow([value,val_dec,res_str,random_date,res_str,random_date,value,val_dec])

def create_csv_3():
    with open(file_3, 'w', newline="") as csvfile:
        start_date = datetime.date(2020, 1, 1)
        end_date = datetime.date(2020, 2, 1)
        time_between_dates = end_date - start_date
        days_between_dates = time_between_dates.days
        for _ in range(a):
            value = random.randint(0, 100)
            val_dec=decimal.Decimal(random.randrange(1, 99999))/100
            res_str = ''.join(random.choices(string.ascii_uppercase + string.digits, k=N))
            random_number_of_days = random.randrange(days_between_dates)
            random_date = start_date + datetime.timedelta(days=random_number_of_days)
            spamwriter = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            spamwriter.writerow([value,val_dec,res_str,random_date,res_str,random_date,value,val_dec])

def create_csv_4():
    with open(file_4, 'w', newline="") as csvfile:
        start_date = datetime.date(2020, 1, 1)
        end_date = datetime.date(2020, 2, 1)
        time_between_dates = end_date - start_date
        days_between_dates = time_between_dates.days
        for _ in range(a):
            value = random.randint(0, 100)
            val_dec=decimal.Decimal(random.randrange(1, 99999))/100
            res_str = ''.join(random.choices(string.ascii_uppercase + string.digits, k=N))
            random_number_of_days = random.randrange(days_between_dates)
            random_date = start_date + datetime.timedelta(days=random_number_of_days)
            spamwriter = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            spamwriter.writerow([value,val_dec,res_str,random_date,res_str,random_date,value,val_dec])

def create_csv_5():
    with open(file_5, 'w', newline="") as csvfile:
        start_date = datetime.date(2020, 1, 1)
        end_date = datetime.date(2020, 2, 1)
        time_between_dates = end_date - start_date
        days_between_dates = time_between_dates.days
        for _ in range(a):
            value = random.randint(0, 100)
            val_dec=decimal.Decimal(random.randrange(1, 99999))/100
            res_str = ''.join(random.choices(string.ascii_uppercase + string.digits, k=N))
            random_number_of_days = random.randrange(days_between_dates)
            random_date = start_date + datetime.timedelta(days=random_number_of_days)
            spamwriter = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            spamwriter.writerow([value,val_dec,res_str,random_date,res_str,random_date,value,val_dec])

t1=Thread(target=create_csv)
t2=Thread(target=create_csv_2)
t3=Thread(target=create_csv_3)
t4=Thread(target=create_csv_4)
t5=Thread(target=create_csv_5)

t1.start()
t2.start()
t3.start()
t4.start()
t5.start()