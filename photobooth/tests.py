from django.test import TestCase
from .models import User,Images,tags

# Create your tests here.
class UserTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.james= User(first_name = 'James', last_name ='Muriuki', email ='james@moringaschool.com')

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.james,User))

        # Testing Save Method
    def test_save_method(self):
        self.james.save_user()
        users = User.objects.all()
        self.assertTrue(len(users) > 0)
