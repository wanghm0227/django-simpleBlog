from django.shortcuts import get_object_or_404, redirect
from django.views import generic
from .models import Post, Category
from .forms import PostForm
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib import messages


# Home page.


class HomeView(generic.ListView):
    model = Post
    template_name = 'myBlog/home.html'


# Read a post.
class ArticleDetailView(generic.DetailView):
    model = Post
    template_name = 'myBlog/article_detail.html'


# Add a new post.


class AddPostView(generic.CreateView):
    model = Post
    form_class = PostForm
    template_name = 'myBlog/add_post.html'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.author = User.objects.get(id=self.request.user.id)
        post.save()
        return redirect('article_detail', post.pk)

# Edit a post.


class UpdatePostView(generic.UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'myBlog/update_post.html'

# Delete a post.


class RemovePostView(generic.DeleteView):
    model = Post
    template_name = 'myBlog/remove_post.html'
    success_url = reverse_lazy('home')

# Add a new category.


class AddCategoryView(generic.CreateView):
    model = Category
    template_name = 'myBlog/add_category.html'
    fields = '__all__'

# List all posts by category.


class CategoryPostsView(generic.ListView):
    model = Post
    template_name = 'myBlog/category_posts.html'

    def get_context_data(self, **kwargs):
        posts_list = Post.objects.filter(category=self.kwargs['category'])
        context = super().get_context_data(**kwargs)
        context['posts_list'] = posts_list
        return context


def like(request, post_id):
    if not request.user.is_authenticated:
        messages.error(request, 'Please login!')
        return redirect('article_detail', post_id)
    post = get_object_or_404(Post, pk=post_id)
    user = User.objects.get(pk=request.user.id)
    post.likes.add(user)
    return redirect('article_detail', post_id)
