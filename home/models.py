from django.db import models

# Create your models here.
class Blog(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    meta = models.CharField(max_length=300)
    content = models.TextField()
    thumbnail_img = models.ImageField(null=True, blank=True, upload_to="images/")
    thumbnail_url = models.URLField(blank=True, null=True)
    category = models.CharField(max_length=255, default="uncategorized")
    slug = models.CharField(max_length=100)
    time = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

class Technology(models.Model):
    item = models.CharField(max_length=50)
    
    def __str__(self):
        return self.item
    
class Project(models.Model):
    pro_title = models.CharField(max_length=200)
    pro_desc = models.TextField(max_length=300)
    pro_spec = models.TextField(max_length=500)
    pro_tech = models.ManyToManyField(Technology)
    pro_git = models.URLField()
    pro_thumb = models.URLField()
    
    def get_pro_spec_list(self):
        return self.pro_spec.split(', ')
    def __str__(self):
        return self.pro_title