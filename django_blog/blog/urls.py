from django.urls import path
#from . import views
from .views import *

urlpatterns = [
    #path('', views.home, name="home"),
    path('', HomeView.as_view(), name="home"),
    path('article/<int:pk>', ArticleDetailView.as_view(), name='article_detail'),
    path('add_blog/', AddPostView.as_view(), name='add_blog'),
    path('add_category/', AddCategoryView.as_view(), name='add_category'),
    path('article/edit/<int:pk>/', UpdatePostView.as_view(), name='update_blog'),
    path('article/edit/<int:pk>/remove', DeletePostView.as_view(), name='delete_blog'),
    path('category/<str:categs>', CategoryView, name='category'),
    path('category-list/', CategoryListView, name='category-list'),
    path('like/<int:pk>', LikeView, name='like_post'),
    path('article/<int:pk>/add_comment', AddCommentView.as_view(), name='add_comment'),
    path('article/<int:pk1>/comment/edit/<int:pk2>', CommentView.as_view(), name='comment'),
    path('article/comment/edit/<int:pk>/remove', DeleteCommentView.as_view(), name='delete_comment'),
    path('searched_article/', SearchedView , name='search-blog'),
]
