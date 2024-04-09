from django.db import models

# Create your models here.



class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'categories'

class Post(models.Model):
    title = models.CharField(max_length=3000)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)  # Removed default value
    image = models.ImageField(upload_to='uploads/post/', blank=False, null=False)
    check_1 = models.BooleanField(default=False)
    step_1 = models.TextField(default='', blank=False, null=False)
    code_1 = models.TextField(default='', blank=False, null=False)
    image_2 = models.ImageField(upload_to='uploads/post/', blank=True, null=True)
    check_2 = models.BooleanField(default=False)
    step_2 = models.TextField(default='', blank=True, null=True)
    code_2 = models.TextField(default='', blank=True, null=True)
    image_3 = models.ImageField(upload_to='uploads/post/', blank=True, null=True)
    check_3 = models.BooleanField(default=False)
    step_3 = models.TextField(default='', blank=True, null=True)
    code_3 = models.TextField(default='', blank=True, null=True)
    image_4 = models.ImageField(upload_to='uploads/post/', blank=True, null=True)
    check_4 = models.BooleanField(default=False)
    step_4 = models.TextField(default='', blank=True, null=True)
    code_4 = models.TextField(default='', blank=True, null=True)
    image_5 = models.ImageField(upload_to='uploads/post/', blank=True, null=True)
    check_5 = models.BooleanField(default=False)
    step_5 = models.TextField(default='', blank=True, null=True)
    code_5 = models.TextField(default='', blank=True, null=True)
    check_5 = models.BooleanField(default=False)
    step_5 = models.TextField(default='', blank=True, null=True)
    code_5 = models.TextField(default='', blank=True, null=True)
    check_6 = models.BooleanField(default=False)
    step_6 = models.TextField(default='', blank=True, null=True)
    code_6 = models.TextField(default='', blank=True, null=True)
    check_7 = models.BooleanField(default=False)
    step_7 = models.TextField(default='', blank=True, null=True)
    code_7 = models.TextField(default='', blank=True, null=True)
    check_8 = models.BooleanField(default=False)
    step_8 = models.TextField(default='', blank=True, null=True)
    code_8 = models.TextField(default='', blank=True, null=True)
    check_9 = models.BooleanField(default=False)
    step_9 = models.TextField(default='', blank=True, null=True)
    code_9 = models.TextField(default='', blank=True, null=True)
    tags = models.TextField(default='', blank=True, null=True)
    source_code = models.URLField(max_length=10000, blank=True, null=True) #<----এটি মানে হল ফিল্ডটি ফর্মে একটি মান প্রবেশ করার জন্য বাধ্যতা নেই। অর্থাৎ, ফিল্ডটি খালি অথবা মান না দিয়েও ফর্ম সাবমিট করা যাবে।
    upload_in = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ('-upload_in',)
    
    def __str__(self):
        return self.title
    

    
    



    





