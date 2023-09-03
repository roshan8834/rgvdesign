from django.db import models
class InteriorService(models.Model):
    title=models.CharField(max_length=50,default="Our Services")
    service_icon=models.CharField(max_length=50)
    service_heading=models.CharField(max_length=100)
    service_desc=models.TextField()

class ProjectCategory(models.Model):
    title=models.CharField(max_length=50,default="Our Portfolio")
    category=models.CharField(max_length=50)
    display_name=models.CharField(max_length=100)
    filter_name=models.CharField(max_length=50,default="filter-res")

    def __str__(self) -> str:
        return self.category

class InteriorProjects(models.Model):
    category=models.ForeignKey(ProjectCategory,on_delete=models.CASCADE,default=1)
    name=models.CharField(max_length=100)
    full_address=models.CharField(max_length=150)
    short_address=models.CharField(max_length=50)
    description=models.CharField(max_length=200)
    project_value=models.IntegerField(default=0)
    cover_image=models.ImageField(upload_to='project_image/',max_length=250,null=True,default=None)

    def __str__(self) -> str:
        return self.name

class ProjectImage(models.Model):
    project=models.ForeignKey(InteriorProjects,on_delete=models.CASCADE)
    image=models.ImageField(upload_to='project_image/',max_length=250,null=True,default=None)
    def __str__(self) -> str:
        return self.project.name

class HeroSection(models.Model):
    heading=models.CharField(max_length=100)
    description=models.TextField()
    image=models.ImageField(upload_to='hero_image/',max_length=250,null=True,default=None)

    def __str__(self) -> str:
        return self.heading

class AboutSection(models.Model):
    title=models.CharField(max_length=100)
    heading=models.CharField(max_length=100)
    description=models.TextField()
    about_me=models.TextField()
    about_me_more=models.TextField()
    
class OurPartner(models.Model):
    name=models.CharField(max_length=50)
    logo=models.ImageField(upload_to='logo_image/',max_length=250,null=True,default=None)
    def __str__(self) -> str:
        return self.name
    

class EnquiryData(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    phone_number=models.CharField(max_length=15)
    subject=models.CharField(max_length=100)
    message=models.TextField()

    def __str__(self) -> str:
        return self.name




    


# Create your models here.
