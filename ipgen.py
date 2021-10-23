from faker import Faker

def ipgen():
    faker = Faker()
    ip = faker.ipv4_public(network=False)
    return ip