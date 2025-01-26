from faker import Faker

fake = Faker()
class DataGenerator:
    valid_city = fake.city()
    valid_country = fake.country()