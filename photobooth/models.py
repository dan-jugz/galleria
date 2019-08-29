from django.db import models
import datetime as dt
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q

class User(models.Model):
    first_name = models.CharField(max_length =30)
    last_name = models.CharField(max_length =30)
    email = models.EmailField()
    phone_number = models.CharField(max_length = 10,blank =True)

    def __str__(self):
        return self.first_name
    class Meta:
        ordering = ['first_name']

    def save_user(self):
        self.save()

class Location(models.Model):
    loc_name=models.CharField(max_length=100)

    def __str__(self):
        return self.loc_name

    
    def save_loc(self):
        self.save() 

    def delete_loc(self):  
        self.delete() 

class Category(models.Model):
    category_name=models.CharField(max_length=50)


    def __str__(self):
        return self.category_name

    def save_category(self):
        self.save() 

    def delete_category(self):
        self.delete()

class tags(models.Model):
    name=models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Image(models.Model):
    title = models.CharField(max_length =60)
    post = models.CharField(max_length =100)
    img_loc=models.ForeignKey(Location,on_delete=models.DO_NOTHING)
    img_category=models.ForeignKey(Category,on_delete=models.DO_NOTHING)
    user = models.ForeignKey('User',on_delete=models.CASCADE)
    tags = models.ManyToManyField(tags)
    pub_date = models.DateTimeField(auto_now_add=True)
    article_image = models.ImageField(upload_to = 'images/',default='')

    @classmethod
    def todays_images(cls):
        today = dt.date.today()
        image = cls.objects.all()
        return image

    @classmethod
    def days_image(cls,date):
        image = cls.objects.filter(pub_date__date = date)
        return image
    
    @classmethod
    def search_by_title(cls,search_term):
        image = cls.objects.filter(title__icontains=search_term)
        return image

    def __str__(self):
        return f'Image{self.title}-{self.img_loc}-{self.img_category}-{self.pub_date}'

    @classmethod
    def get_photos(cls):
        photos=cls.objects.order_by('pub_date')

        return photos

    @classmethod
    def search_by_category(cls,search_term):
        #Using lookup that spans relations to fetch for all photos with a searched keyword regardless of case
        photos=cls.objects.filter( Q(img_category__category_name__iexact=search_term) | 
        Q(img_loc__loc_name__icontains=search_term) | Q(img_name__icontains=search_term)  | Q(author__first_name__icontains=search_term))

        return photos  

    @classmethod
    def filter_by_location(cls,location):

        photos=cls.objects.filter(img_loc__loc_name__icontains=location)
        return photos

    @classmethod
    def get_img_by_id(cls,img_id):
        pic=cls.objects.get(pk=img_id)
        return pic

    
    @classmethod
    def delete_photo():
        pass  