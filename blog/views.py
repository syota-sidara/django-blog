from django.views.generic import ListView
from .models import Post
# Create your views here.

# 一覧画面
class PostListView(ListView):
  model = Post
  template_name = 'blog/home.html'
  context_object_name = 'posts'
  ordering = ['-date_posted']
