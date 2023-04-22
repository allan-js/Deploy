from django.db import models

# Site Management DB Models
class Banner(models.Model):
    name = models.CharField(max_length=50, verbose_name='Banner Image Name')
    image = models.ImageField(upload_to='Images/Banners/%Y/%M/%d', help_text='Upload you images to show up on the page front')
    tagline = models.CharField(max_length=255, help_text='Tagline text is shown on top of the banner image')
    is_active = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Staff(models.Model):
    full_name = models.CharField(max_length=125, verbose_name='Full Name')
    role = models.CharField(max_length=75, verbose_name='Roles')
    photo = models.ImageField(upload_to='Images/Staff/%Y/%M')
    about = models.TextField()
    is_active = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Staff'
        verbose_name_plural = 'Staff'


    def __str__(self):
        return self.full_name


class Meal(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='Images/Meals/%Y/%M/%d')
    description = models.TextField()
    price = models.DecimalField(max_digits=9, decimal_places=2)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Room(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='Images/Rooms/%Y/%M/%d')
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=9)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    is_taken = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class GalleryImage(models.Model):
    name = models.CharField(max_length=75, verbose_name='Image Name', help_text='Image name describes the image')
    image = models.ImageField(upload_to="Gallery/Images/%Y/%M/%d")
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Gallery Image'
        verbose_name_plural = 'Gallery Images'

    def __str__(self):
        return str(f'Image Uploaded on {self.created}')


class BaseInfo(models.Model):
    email = models.EmailField()
    email2 = models.EmailField()
    telephone = models.CharField(max_length=13)
    other_phone = models.CharField(max_length=13)
    address = models.CharField(max_length=255)
    address2 = models.CharField(max_length=255)
    about_KHM = models.TextField()
    image = models.ImageField(upload_to='Images/BaseInfo')
    image2 = models.ImageField(upload_to='Images/BaseInfo')
    welcome_image = models.ImageField(upload_to='Images/BaseInfo')

    class Meta:
        verbose_name = 'Base Info'
        verbose_name_plural = 'Base Info'

    def __str__(self):
        return str(self.email)
    
    
class Document(models.Model):
    name = models.CharField(max_length=75, verbose_name='Document Name', help_text='format: text. Name of the Document')
    description = models.TextField(verbose_name='File Description', help_text='format: text. Write a description of the associated file!')
    file = models.FileField(upload_to='Files/%Y/%M/%d', help_text='format: txt, pdf, img, png. jpg, jpeg, audio. Upload your intented file')
    is_active = models.BooleanField(default=True, help_text='Designate whether the document is active for use and download.')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    def __str__(self):
        return str(self.name)