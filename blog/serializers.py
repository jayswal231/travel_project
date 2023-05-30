from .models import *
from rest_framework import serializers
from collections import OrderedDict
from datetime import datetime
from rest_framework import serializers
from datetime import datetime
from .models import *



class Comment_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

class CommentMeta_Serializer(serializers.ModelSerializer):
    class Meta:
        model = CommentMeta
        fields = '__all__'

class Author_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'


from dateutil import parser
def format_date(date):
    date = parser.parse(date).date()
    formatted_date = date.strftime('%B %d, %Y')
    return formatted_date

    
class Post_Serializer(serializers.ModelSerializer):
    def to_representation(self, instance):
        response = super(Post_Serializer, self).to_representation(instance)
        post_date = response.pop('post_date')
        post_date_gmt = response.pop('post_date_gmt')
        post_modified = response.pop('post_modified')
        post_modified_gmt = response.pop('post_modified_gmt')
        # response['get_absolute_url'] = instance.get_absolute_url
        response['post_date'] = format_date(post_date)
        response['post_date_gmt'] = format_date(post_date_gmt)
        response['post_modified'] = format_date(post_modified)
        response['post_modified_gmt'] = format_date(post_modified_gmt)
        return response
    
    class Meta:
        model = Post
        exclude = ['post_password','post_name','to_ping','pinged','post_content_filtered','post_parent','guid','menu_order','post_type','post_mime_type']
        


class PostMeta_Serializer(serializers.ModelSerializer):
    class Meta:
        model = PostMeta
        fields = '__all__'

class Term_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Term
        fields = '__all__'

class TermMeta_Serializer(serializers.ModelSerializer):
    class Meta:
        model = TermMeta
        fields = '__all__'

class Category_Serializer(serializers.ModelSerializer):
     class Meta:
        model = Category
        fields = '__all__'

class Option_Serializer(serializers.ModelSerializer):
     class Meta:
        model = Option
        fields = '__all__'

class Link_Serializer(serializers.ModelSerializer):
     class Meta:
        model = Link
        fields = '__all__'

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'




# for blog view count

class UrlViewSerializer(serializers.ModelSerializer):
    
    def to_representation(self, instance):
        context = super().to_representation(instance)

        # checking to see if it a post or not
        if ("post" in instance.url):
            context["post"] = True
        
        return context
    
    class Meta:
        model = UrlView
        fields = '__all__'
        
class PostViewSerializer(serializers.ModelSerializer):
    post = Post_Serializer()

    class Meta:
        model = PostView
        exclude = ['counter']
