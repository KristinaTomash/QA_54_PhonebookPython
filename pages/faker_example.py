from faker import Faker
from numpy.ma.extras import unique

fake = Faker()

print(fake.first_name())
print(fake.last_name())

print(fake.street_address())
print(fake.phone_number())
print(fake.sentence())

print(fake.email())

print(fake.unique.email())

print(fake.numerify(text="05#########"))
