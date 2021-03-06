from django.core.exceptions import ViewDoesNotExist
from  django.urls import path
from .views import AddCategory, Addp, HomePage,BlogD,UpdateViewB,DeleteViewB
from . import views


urlpatterns = [
  # path('', views.home, name='home',),
  path('', HomePage.as_view(), name='home'),
  path('blog/<int:pk>', BlogD.as_view(), name='blog_detail' ),
  path('add_photo/',Addp.as_view(), name='addphoto'),
  path('add_category/',AddCategory.as_view(), name='addcategory'),
  path('article/edit/<int:pk>', UpdateViewB.as_view(), name="updateb"),
  path('article/<int:pk>/delete',  DeleteViewB.as_view(), name="deleteb"),
  path('search', views.search_blog,name='search_blog')
]