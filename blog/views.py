from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated,AllowAny,IsAuthenticatedOrReadOnly
from django.shortcuts import get_list_or_404, get_object_or_404
from .models import *
from .serializers import *
from rest_framework import viewsets
from rest_framework.response import Response
from django.db.models import Count
from rest_framework.generics import ListAPIView



class CommentViewset(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = Comment_Serializer
    # permission_classes = [IsAuthenticatedOrReadOnly]

class CommentMetaViewset(viewsets.ModelViewSet):
    queryset = CommentMeta.objects.all()
    serializer_class = CommentMeta_Serializer

class AuthorViewset(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = Author_Serializer


class PostViewset(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = Post_Serializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    

class PostMetaViewset(viewsets.ModelViewSet):
    queryset = PostMeta.objects.all()
    serializer_class = PostMeta_Serializer

class Term_Viewset(viewsets.ModelViewSet):
    queryset = Term.objects.all()
    serializer_class = Term_Serializer

class TermMeta_Viewset(viewsets.ModelViewSet):
    queryset = TermMeta.objects.all()
    serializer_class = TermMeta_Serializer


class CategoryViewset(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = Category_Serializer
    lookup_field = "slug"
    
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    def retrieve(self, request, slug=None):
        # print(slug)
        category = get_object_or_404(Category, slug=slug)
        serializer = self.serializer_class(category)
        return Response(serializer.data)

class OptionViewset(viewsets.ModelViewSet):
    queryset = Option.objects.all()
    serializer_class = Option_Serializer

class LinkViewset(viewsets.ModelViewSet):
    queryset = Link.objects.all()
    serializer_class = Link_Serializer

class ContactViewset(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer





# for blog view  count

class UrlviewViewSet(viewsets.ModelViewSet):
    queryset = UrlView.objects.all()
    serializer_class = UrlViewSerializer   
    
    def create(self, request, *args, **kwargs):
        data = request.data

        url  = data['url']
        url_view,created = UrlView.objects.get_or_create(url=url)
        
        url_view.counter += 1
        url_view.save()
        
        serializer = UrlViewSerializer(url_view)
        print('finish')
        
        if data['post_slug'] == True:
            post_id = data['post_slug']
            post = Post.objects.get(id=post_id)
            post_view,created = PostView.objects.get_or_create(post=post)
            post_view.counter += 1
            post_view.save()
    
            serializer = PostViewSerializer(post_view).data
        
            return Response({"response": "postview count update successfully","data":serializer})
        
            
class PostTrendingViewSet(viewsets.ReadOnlyModelViewSet): 
    queryset = PostView.objects.all()
    serializer_class = PostViewSerializer
    

    def get_queryset(self):
        return PostView.objects.annotate(num=Count('counter')).order_by('-counter')       