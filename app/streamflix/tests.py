import pytest 
from models import Account

def test_create_account():
    new_account = Account.objects.create(id='1',
        email='brookslanden@gmail.com',
        password='admin1234')
    assert new_account.id == '1'

def test_search_account():
    Account.objects.create(id='1',
        email='brookslanden@gmail.com',
        password='admin1234')
    assert Account.objects.filter(id='1')