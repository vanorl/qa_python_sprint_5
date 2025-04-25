from faker import Faker
import random

faker = Faker()

def generate_registration_data(short_pass=False):
    name = faker.first_name()
    email = f'ivanorlov21{random.randint(111, 999)}@yandex.ru'

    if short_pass:
        password = faker.password(length=5, special_chars=False, digits=True, upper_case=True, lower_case=True)
    else:
        password = faker.password(length=12, special_chars=False, digits=True, upper_case=True, lower_case=True)

    return name, email, password
