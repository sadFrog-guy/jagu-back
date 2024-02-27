from django.db import models
from django.core.validators import FileExtensionValidator
from ckeditor.fields import RichTextField

default_number = '+996 222-31-01-61'

class Employee(models.Model):
    first_name = models.CharField(max_length=50)
    second_name = models.CharField(max_length=50)
    specialization = models.CharField(max_length=1000)
    photo = models.FileField(
        upload_to='static/cafedra/header_img/',
        validators=[FileExtensionValidator(['png', 'jpg', 'jpeg'])])
    
    pdf_file = models.FileField(
        upload_to='static/cafe+dra/pdfs/',
        validators=[FileExtensionValidator(['pdf'])],)

    def __str__(self):
        return self.first_name + " " + self.second_name
     
class FileModel(models.Model):
    file = models.FileField(
        upload_to='static/cafedra/pdfs/',
        validators=[FileExtensionValidator(['pdf'])],)
    title = models.CharField(max_length=23)

    def __str__(self) :
        return self.title

class InfoPage(models.Model):
    page_name = models.CharField('Название страницы', max_length=20, default='Название')
    header = models.CharField('Заголовок',   max_length=80)
    subheader = models.CharField('Под загаловок', max_length=150)
    info_text = RichTextField()
    header_img = models.FileField(
        upload_to='static/cafedra/header_img/',
        validators=[FileExtensionValidator(['png', 'jpg', 'jpeg'])])
    slug = models.SlugField('слег-сайта', unique=True, blank=True)

    def __str__(self):
        return self.header

class EmployeePage(models.Model):
    page_name = models.CharField('Название страницы', max_length=20, default='Название')
    header = models.CharField('Заголовок', max_length=80)
    subheader = models.CharField('Под загаловок', max_length=150)
    employes_list = models.ManyToManyField(Employee)
    img = models.FileField(
        upload_to='static/cafedra/header_img/',
        validators=[FileExtensionValidator(['png', 'jpg', 'jpeg'])])
    slug = models.SlugField('слег-сайта', unique=True, blank=True)

    def __str__(self) -> str:
        return self.header

class FilePage(models.Model):
    page_name = models.CharField('Название страницы', max_length=20, default='Название')
    heading = models.CharField('Заголовок',   max_length=80)
    subheading = models.CharField('Под загаловок', max_length=150)
    img = models.FileField(
        default='static/cafedra/header_img/bg.jpg',
        upload_to='static/cafedra/header_img/',
        validators=[FileExtensionValidator(['png', 'jpg', 'jpeg'])])
    file_list = models.ManyToManyField(FileModel)
    slug = models.SlugField('слег-сайта', unique=True)

    def __str__(self):
        return self.heading
    

class MainPage(models.Model):
    title_university = models.CharField(max_length=75)
    name = models.CharField(max_length=40)
    position = models.CharField(max_length=30)
    short_info = models.CharField(max_length=300)
    summary = models.FileField(
        upload_to='static/cafedra/pdfs/',
        validators=[FileExtensionValidator(['pdf'])],)
    address = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=25, default=default_number)
    email = models.CharField(max_length=40)
    photo_deportament = models.FileField(
        upload_to='static/main_img/',
        default='static/cafedra/header_img/bg.jpg',
        validators=[FileExtensionValidator(['png', 'jpg', 'jpeg'])])

    photo = models.ImageField(upload_to ='static/main_img/')

    def save(self, *args, **kwargs):
        self.title_university = self.title_university.upper()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name