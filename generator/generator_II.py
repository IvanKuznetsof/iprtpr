import csv
import random
import string
from datetime import datetime, timedelta
import time

def generate_full_name():
    cyrillyc_alpha_lower = ['а','б','в','г','д','е','ё','ж','з','и','й','к','л','м','н','о','п','р','с','т','у','ф','х','ц','ч','ш','щ','ъ','ы','ь','э','ю','я']
    
    first_name = ''.join(random.choices(cyrillyc_alpha_lower, k=random.randint(3, 10)))
    first_name = string.capwords(first_name)
    
    last_name = ''.join(random.choices(cyrillyc_alpha_lower, k=random.randint(3, 10)))
    last_name = string.capwords(last_name)
    
    middle_name = ''.join(random.choices(cyrillyc_alpha_lower, k=random.randint(3, 10)))
    middle_name = string.capwords(middle_name)
    
    return f"{last_name}ев {first_name}ибек {middle_name}аевич"

def generate_birth_date():
    current_date = datetime.now()
    birth_date = current_date - timedelta(days=random.randint(18*365, 99*365))
    return birth_date.strftime('%d.%m.%Y')

def generate_phone_number(used_numbers):
    number = '8999' + ''.join(random.choices(string.digits, k=7))
    while number in used_numbers:
        number = '8999' + ''.join(random.choices(string.digits, k=7))
    used_numbers.add(number)
    return number

def generate_email():
    letters = string.ascii_lowercase
    username = ''.join(random.choices(letters, k=random.randint(5, 10)))
    domain = random.choice(['mail.ru','yandex.ru','gmail.com', 'krovatka.com', 'ahhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh.com', 'govnosite.by', 'kaka.com', 'mozgov.net', 'pipec.com'])
    return f"{username}@{domain}"

def generate_snils():
    region = random.randint(1, 99)
    gender = random.randint(0, 1)
    number = random.randint(100000000, 999999999)
    snils = f"{region:02}{gender}{number:09}"
    control_sum = 0
    for i in range(9):
        control_sum += int(snils[i]) * (9 - i)
    control_sum %= 101
    if control_sum == 100:
        control_sum = 0
    return f"{snils}{control_sum:02}"

def generate_records(num_records):
    used_numbers = set()
    records = []
    for _ in range(num_records):
        full_name = generate_full_name()
        birth_date = generate_birth_date()
        phone_number = generate_phone_number(used_numbers)
        email = generate_email()
        snils = generate_snils()
        records.append([full_name, birth_date, phone_number, email, snils])
        

    return records

def write_to_csv(records, file_name):
    with open(file_name, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['ФИО', 'Дата рождения', 'Номер телефона', 'Электронная почта', 'СНИЛС'])
        for record in records:
            writer.writerow(record)

num_records = int(input('Введите целое число, обозначающее размер пула:\n'))
filename = input('Введите желаемое имя файла\n')
unique = time.time()
final_name = f'{unique}_{filename}.csv'

records = generate_records(num_records)
write_to_csv(records, final_name)