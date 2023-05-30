
from blog.views import *
from django.urls import path,include

from travel.urls import router


router.register('comment', CommentViewset,basename='comment')
router.register('post', PostViewset,basename='post')
router.register('category', CategoryViewset,basename='category')
router.register('contact', ContactViewset,basename='contact')

# for blog view count
router.register('urlview', UrlviewViewSet,basename='urlview')
router.register('post-trending', PostTrendingViewSet,basename='post-trending')

urlpatterns = [
    path('api/', include(router.urls)),
   
]