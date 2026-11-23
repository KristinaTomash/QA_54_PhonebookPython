import random
import logging
from faker import Faker
from models.contact import Contact
from pages.add_contact_page import ContactPage

fake = Faker()
logger = logging.getLogger(__name__)
def test_add_contact_success(authenticated):
    logger.info(f"test_add_contact_success")
    contact_page = ContactPage(authenticated)
    contact_page = ContactPage(authenticated)
    random_suffix = random.randint(10000,1000000)

    contact = Contact(
        name = fake.first_name(),
        last_name = fake.last_name(),
        phone=f"05435{random_suffix}",
        email=f"test_{random_suffix}@gm.com",
        address=fake.street_address(),
        description=fake.sentence(nb_words=4)
    )
    contact_page.create_contact_steps(contact)

    assert contact_page.contact_card_visible(contact.phone)

def test_add_contact_success_all_req_fields(authenticated):
    contact_page = ContactPage(authenticated)
    random_suffix = random.randint(10000,1000000)

    contact = Contact(
        name = fake.first_name(),
        last_name = fake.last_name(),
        #phone= f"05435{random_suffix}",
        phone=fake.numerify("05#########"),
        email=fake.email(),
        address=fake.street_address(),
        description=""
    )
    contact_page.create_contact_steps(contact)

    assert contact_page.contact_card_visible(contact.phone)