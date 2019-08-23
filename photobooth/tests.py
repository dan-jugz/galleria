from django.test import TestCase
from .models import User,Images,tags

# Create your tests here.
class UserrTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.james= User(first_name = 'James', last_name ='Muriuki', email ='james@moringaschool.com')
