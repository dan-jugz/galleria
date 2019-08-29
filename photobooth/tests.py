from django.test import TestCase
from .models import User,Image,tags,Location,Category
import datetime as dt

class UserTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.daniel= User(first_name = 'Daniel', last_name ='Njuguna', email ='njuguna@moringaschrienl.com')

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.daniel,User))

        # Testing Save Method
    def test_save_method(self):
        self.daniel.save_user()
        users = User.objects.all()
        self.assertTrue(len(users) > 0)

class CategoryTestClass(TestCase):

    #set up method
    def setUp(self):
        self.friend=Category(category_name='Friend')

    #Testing Instance
    def test_instance(self):
        self.assertTrue(isinstance(self.friend,Category))   

     #Testing save method
    def test_save_method(self):
        self.friend.save_category()
        categories=Category.objects.all()
        self.assertTrue(len(categories)>0)  

    #Testing save multiple
    def test_save_multiple_categories(self):
        self.friend.save_category()

        test_drug=Category(category_name='Drugs')
        test_drug.save_category()

        categories=Category.objects.all()
        self.assertEqual(len(categories),2)


    #Testiing delete method
    def test_delete_method(self):
        self.friend.save_category()

        test_drug=Category(category_name='Drugs')
        test_drug.save_category()

        test_drug.delete_category()
        categories=Category.objects.all()
        self.assertEqual(len(categories),1)

class LocationTestClass(TestCase):

    #set up method
    def setUp(self):
        self.kenya=Location(loc_name='Nairobi')

    #Testing Instance
    def test_instance(self):
        self.assertTrue(isinstance(self.kenya,Location))   

     #Testing save method
    def test_save_method(self):
        self.kenya.save_loc()
        locations=Location.objects.all()
        self.assertTrue(len(locations)>0)  

    #Testing save multiple
    def test_save_multiple_locations(self):
        self.kenya.save_loc()

        test_nai=Location(loc_name='Nairobi')
        test_nai.save_loc()

        locations=Location.objects.all()
        self.assertEqual(len(locations),2)


    #Testiing delete method
    def test_delete_method(self):
        self.kenya.save_loc()

        test_nai=Location(loc_name='Nairobi')
        test_nai.save_loc()

        test_nai.delete_loc()
        locations=Location.objects.all()
        self.assertEqual(len(locations),1)

class ImageTestClass(TestCase):

    def setUp(self):
        # Creating a new editor and saving it
        self.daniel= User(first_name = 'Daniel', last_name ='Njuguna', email ='njuguna@moringaschrienl.com')
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
    
    def test_delete_photo(self):
        self.new_img.save()
        self.new_img.tags.add(self.new_tag)  

        test_user=User(first_name='pooh',last_name="bear",email='pooh@bear.com')   
        test_user.save_user()

        test_food=Category(category_name='Honey')
        test_food.save_category()

        test_kis=Location(loc_name='Kisii')
        test_kis.save_loc()

        #creating a new tag and saving it
        test_food_tag=tags(tag_name='#sweet')
        test_food_tag.save()

        test_img=Image(img_name='Sweet Food',img_desc='Sweet burger 89-21',img_loc=test_kis,img_category=test_food,author=test_user)
        test_img.save()

        test_img.tags.add(test_food_tag)  
        
        images=Image.objects.all()
        test_img.delete_photo()
        self.assertEqual(len(images),1)