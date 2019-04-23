from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length = 255)
    pub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='images/blog_image')



#Create a Blog models
# title
#pub_date
#body
#image# Create your models here.
