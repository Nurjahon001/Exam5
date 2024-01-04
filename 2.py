from faker import Faker
from random import  randint
faker = Faker()
with open('text1.txt',"w") as t1:
    for i in range(1,6):
        t1.write(f"{i}.{faker.name()}-{randint(18,100)} \n")