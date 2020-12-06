from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from rest_framework.utils.mediatypes import order_by_precedence

from blog.models import Post
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/index.html', context)


# here i am inheriting from list view which i imported at the top
# this is a class base view
# this type of view can do more than what a function base view can do
# this list view enable us to list our files the way we want it to be
class PostListView(ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5


class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html'
    context_object_name = 'posts'
    paginate_by = 5

    # this is for a user view in which if
    #  you click a username it takes you to all his post
    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('date_posted')

"""
 this class based view can be used without putting a template name
  because a template name already exist in the urls so i don't really need it
   """


class PostDetailView(DetailView):
    model = Post


"""
 this class based view can be used to create a form without going to form
 to create it but you need to use the fields
but when you create a form in a class base view you know that the form does not have
 an author that means you have to create a function that enables django to know which user is creating this form
and note the url of this PostCreateView is post/new/ that is how django wants it to ber
this LoginRequiredMixin is just like the decorator but this is how it is use in a class based view 
"""


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']



    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


"""
this is the the view that handles the login required before checking profile
this is the view that handles the update for the user which enables the user to update a file
this is the view that handles when a user tries to
"""


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    # this is the function that enables us to know the user that have the post
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def about(request):
    return render(request, 'blog/about.html')


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
