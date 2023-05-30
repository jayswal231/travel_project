from django.db import models
from django.utils.text import slugify
from django.utils.translation import gettext as _
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

# Create your models here.

class Comment(models.Model):
    comment_post_Id = models.BigIntegerField()
    comment_author = models.TextField()
    comment_author_email = models.CharField(max_length=100)
    comment_author_url = models.CharField(max_length=200)
    comment_author_IP = models.CharField(max_length=100)
    comment_date = models.DateTimeField(auto_now_add=True)
    comment_date_gmt = models.DateTimeField(auto_now_add=True)
    comment_content = models.TextField()
    comment_karma = models.IntegerField()
    comment_approved = models.CharField(max_length=20)
    comment_agent = models.CharField(max_length=255)
    comment_type = models.CharField(max_length=20)
    comment_parent = models.BigIntegerField()
    
    
    def __str__(self):
        return self.comment_author


class CommentMeta(models.Model):
    comment = models.ForeignKey(Comment,on_delete=models.CASCADE)
    meta_key = models.CharField(max_length=255)
    meta_value = models.TextField()

    def __str__(self):
        return self.comment

class Author(models.Model):
    name = models.CharField(max_length=250)
    website = models.CharField(max_length=255)
    facebook = models.CharField(max_length=255)
    instagram = models.CharField(max_length=255)
    linkdin = models.CharField(max_length=255)
   
    
    def __str__(self):
        return self.name

class Term(models.Model):
    name = models.CharField(max_length=200)
    slug = models.CharField(max_length=200)
    term_group = models.BigIntegerField()

    def __str__(self):
        return self.name
class SubCategory(models.Model):
    term_id = models.ForeignKey(Term,on_delete=models.CASCADE)
    category_name = models.CharField(max_length=32)
    description = models.TextField()
    slug = models.CharField(max_length=200)
    parent = models.BigIntegerField()
    count = models.BigIntegerField()

    def __str__(self):
        return self.category_name


    
class Category(models.Model):
    sub_category= models.ForeignKey(SubCategory, null= True, blank= True, on_delete=models.CASCADE)
    name = models.CharField(max_length=100,blank=True, null=True,unique=True)
    slug = models.SlugField(max_length=100, blank=True, unique=True)
    
    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.slug
    

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)


POST_CHOICE = (("Draft","Draft"),("published","published"),("Scheduled","Scheduled"))
class Post(models.Model):
    # user = models.Foreignkey(CustomUser,relative_name = 'user', on_delete = models.CASCADE )
    post_author = models.ForeignKey(Author,null=True, blank=True, on_delete=models.CASCADE) #
    post_date = models.DateTimeField(auto_now_add=True)
    post_date_gmt = models.DateTimeField(auto_now_add=True, null=True, blank=True) #
    post_content = models.TextField()
    post_title = models.TextField()
    post_excerpt = models.TextField()
    reading_time = models.CharField(max_length=100,null=True)
    post_image = models.ImageField(upload_to="upload/post",  max_length=100,null = True, blank= True)
    # post_image = models.URLField(max_length = 200,null = True, blank= True)
    # feature_image = models.URLField(_(""), max_length=200)
    post_status = models.CharField(max_length=20,choices=POST_CHOICE, default="published")
    
    comment_status = models.ForeignKey(Comment,null=True, blank=True, related_name='comment', on_delete=models.CASCADE) #
    
    PING = (("Draft","Draft"),("published","published"),("Scheduled","Scheduled"))
    ping_status = models.CharField(max_length=200,choices=PING,null=True, blank=True, default="published") #
    
    post_password = models.CharField(max_length=20, null=True, blank=True) #
    post_name = models.CharField(max_length=200, null=True, blank=True) #
    to_ping = models.TextField(null=True, blank=True) #
    pinged = models.TextField(null=True, blank=True) #
    post_modified = models.DateTimeField(auto_now=True)
    post_modified_gmt = models.DateTimeField(auto_now_add=True) #
    post_content_filtered = models.TextField(null=True, blank=True) #
    post_parent = models.BigIntegerField(null=True, blank=True) #
    guid = models.CharField(max_length=255, null=True, blank=True) #
    menu_order = models.IntegerField(null=True, blank=True) #
    post_type = models.CharField(max_length=20, null=True, blank=True) #
    post_mime_type = models.CharField(max_length=100, null=True, blank=True) #
    comments_count = models.ForeignKey(Comment, null= True,blank= True, on_delete=models.CASCADE) #
    category_name = models.ForeignKey(Category,on_delete=models.CASCADE) 
    slug = models.SlugField(max_length=100, blank=True,unique=True) 

    class Meta:
        ordering = ['-post_date']
        
    def get_unique_slug(self):
        slug = slugify(self.post_title)
        num = 1
        while Post.objects.filter(slug=slug).exists():
            slug = f'{slug}-{num}'
            num += 1
        return slug
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.post_title)
        while Post.objects.filter(slug=self.slug).exists():
            self.slug = self.get_unique_slug()
        super().save(*args, **kwargs)
    
    # @property
    # def get_absolute_url(self):
    #     return reverse('post_detail', kwargs={'slug': self.slug})


class PostMeta(models.Model):
    post_id = models.ForeignKey(Post,on_delete=models.CASCADE)
    meta_key = models.CharField(max_length=255)
    meta_value = models.TextField()
    
    def __str__(self):
        return self.meta_key
 


class TermMeta(models.Model):
    term_id = models.ForeignKey(Term,on_delete=models.CASCADE)
    meta_key = models.CharField(max_length=255)
    meta_value = models.TextField()

    def __str__(self):
        return self.meta_key



        
class Option(models.Model):
    option_name = models.CharField(max_length=191)
    option_value = models.TextField()
    autoload = models.CharField(max_length=20)

    def __str__(self):
        return self.option_name


class Link(models.Model):
    link_url = models.CharField(max_length=255)
    link_name = models.CharField(max_length=255)
    link_image = models.ImageField(upload_to='images/img')
    link_target = models.CharField(max_length=25)
    link_description = models.TextField()
    link_visible = models.CharField(max_length=20)
    link_owner = models.BigIntegerField()
    link_rating = models.IntegerField()
    link_updated = models.DateTimeField(auto_now_add=True)
    link_ref = models.CharField(max_length=255)
    link_notes = models.TextField()
    link_rss = models.CharField(max_length=255)

    def __str__(self):
        return self.link_name

class Contact(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100,null=True)
    company_name = models.CharField(max_length=100,null=True)
    message = models.TextField()
   



# for blog-view-count

class PostView(models.Model):
    post = models.ForeignKey(Post,on_delete=models.SET_NULL, blank=True, null=True)
    counter = models.PositiveIntegerField(_("PostCounter"),default=0)

    class Meta:
        verbose_name = _("PostView")
        verbose_name_plural = _("PostViews")

    def __str__(self):
        return self.post

    def get_absolute_url(self):
        return reverse("PostView_detail", kwargs={"pk": self.pk})

    

class UrlView(models.Model):

    url = models.URLField(_("URL"), max_length=200, unique=True)
    counter = models.PositiveIntegerField(_("UrlCounter"),default=0)
    
    
    class Meta:
        verbose_name = _("UrlView")
        verbose_name_plural = _("UrlViews")

    def __str__(self):
        return self.url

    def get_absolute_url(self):
        return reverse("UrlView_detail", kwargs={"pk": self.pk})

