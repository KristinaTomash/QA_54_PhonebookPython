import random
import logging

import pytest
from faker import Faker
from models.contact import Contact
from pages.add_contact_page import ContactPage

fake = Faker()
logger = logging.getLogger(__name__)
@pytest.mark.parametrize(
    "phone",
    [
        fake.numerify("05#########"),
        ""
    ]
)

def test_add_contact_success(authenticated, phone):
    logger.info(f"test_add_contact_success")
    contact_page = ContactPage(authenticated)
    random_suffix = random.randint(10000,1000000)
    contact = Contact(
        name = fake.first_name(),
        last_name = fake.last_name(),
        phone=phone,
        email=f"test_{random_suffix}@gm.com",
        address=fake.street_address(),
        description=fake.sentence(nb_words=4)
    )
    contact_page.create_contact_steps(contact)

    assert contact_page.contact_card_visible(contact.phone)

def test_add_contact_success_all_req_fields(authenticated,phone):
    contact_page = ContactPage(authenticated)
    random_suffix = random.randint(10000,1000000)

    contact = Contact(
        name = fake.first_name(),
        last_name = fake.last_name(),
        #phone= f"05435{random_suffix}",
        phone=phone,
        email=fake.email(),
        address=fake.street_address(),
        description=""
    )
    contact_page.create_contact_steps(contact)

    assert contact_page.contact_card_visible(contact.phone)

def test_add_contact_empty_phone_negative(authenticated, phone):
    contact_page = ContactPage(authenticated)
    contact = Contact(
        fake.first_name(),
        fake.last_name(),
        phone,
        fake.email(),
        fake.street_address(),
        fake.sentence(nb_words=2)
    )
    contact_page.create_contact_steps(contact)
    assert contact_page.is_alert_visible()
    assert "Phone number must contain only digits" in contact_page.get_alert_text()
    contact_page.accept_alert()