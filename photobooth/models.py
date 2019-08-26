from django.db import models
import datetime as dt

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

class tags(models.Model):
    name=models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Image(models.Model):
    title = models.CharField(max_length =60)
    post = models.CharField(max_length =100)
    user = models.ForeignKey('User',on_delete=models.CASCADE)
    tags = models.ManyToManyField(tags)
    pub_date = models.DateTimeField(auto_now_add=True)
    article_image = models.ImageField(upload_to = 'images/',default='')

    @classmethod
    def todays_images(cls):
        today = dt.date.today()
        image = cls.objects.filter(pub_date__date = today)
        return image

    @classmethod
    def days_image(cls,date):
        image = cls.objects.filter(pub_date__date = date)
        return image
    
    @classmethod
    def search_by_title(cls,search_term):
        image = cls.objects.filter(title__icontains=search_term)
        return image

