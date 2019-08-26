from django.test import TestCase
from .models import User,Image,tags
import datetime as dt

class UserTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.daniel= User(first_name = 'Daniel', last_name ='Njuguna', email ='njuguna@moringaschool.com')

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.daniel,User))

        # Testing Save Method
    def test_save_method(self):
        self.daniel.save_user()
        users = User.objects.all()
        self.assertTrue(len(users) > 0)
class ImageTestClass(TestCase):

    def setUp(self):
        # Creating a new editor and saving it
        self.daniel= User(first_name = 'Daniel', last_name ='Njuguna', email ='njuguna@moringaschool.com')
        self.daniel.save_user()

        # Creating a new tag and saving it
        self.new_tag = tags(name = 'testing')
        self.new_tag.save()

        self.new_image= Image(title = 'Test Image',post = 'This is a random test Post',user = self.daniel)
        self.new_image.save()

        self.new_image.tags.add(self.new_tag)

    def tearDown(self):
        User.objects.all().delete()
        tags.objects.all().delete()
        Image.objects.all().delete()
    
    def test_get_images_today(self):
        today_news = Image.todays_images()
        self.assertTrue(len(images_today)>0)

    def test_get_images_by_date(self):
        test_date = '2017-03-17'
        date = dt.datetime.strptime(test_date, '%Y-%m-%d').date()
        images_by_date = Image.days_images(date)
        self.assertTrue(len(images_by_date) == 0)