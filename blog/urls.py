from django.urls import path

from blog.views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView,UserPostListView




from . import views

urlpatterns = [
    path('', PostListView.as_view(), name='blog_home'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('about/', views.about, name='blog_about')
]

"""
 note that all the url that has  .as_view is class based view 
  django wants it to be post/new/ and i don't need to create a new html file for this
  
"""
