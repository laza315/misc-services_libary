from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)

# Create your views here.
# dummy data
posts = [
    {
        'author': 'LazarDJ',
        'title': 'Blog Post',
        'content': 'First post content',
        'date_posted': 'October 27, 2023'
    },
    {
        'author': 'JaneD',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'October 28, 2023'
    }
]


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)


class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html' # is looking for <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5


class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html' # is looking for <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username')) # get username from url or return 404
        return Post.objects.filter(author=user).order_by('-date_posted')


class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin,CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user # ovo kaze da formu koju pokusavas da napravis uzmi instancu authora i
        # prepisi je trenutno ulogovanom useru
        return super().form_valid(form) # form valid ce svakako da runuje nad nasom parent classom, ali mi samo joj
        # dodajemo autora pre nego sto se runuje


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user # ovo kaze da formu koju pokusavas da napravis uzmi instancu authora i
        # prepisi je trenutno ulogovanom useru
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object() # get post koji pokusavamo da updatujemo
        if self.request.user == post.author: # uporedi da li je taj post od istog autora
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object() # get post koji pokusavamo da updatujemo
        if self.request.user == post.author: # uporedi da li je taj post od istog autora
            return True
        return False


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
