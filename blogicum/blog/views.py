from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView
from django.utils import timezone

from blog.models import Category, Post

POSTS_PER_PAGE = 10


def get_base_queryset():
    """Возвращает базовый QuerySet."""
    return Post.objects.filter(
        is_published=True,
        pub_date__lte=timezone.now(),
        category__is_published=True
    ).select_related(
        'author', 'location', 'category'
    )


class IndexListView(ListView):
    model = Post
    template_name = 'blog/index.html'
    paginate_by = POSTS_PER_PAGE

    def get_queryset(self):
        return get_base_queryset().order_by('-pub_date')


def post_detail(request, post_id):
    post = get_object_or_404(
        get_base_queryset(),
        id=post_id
    )
    return render(request, 'blog/detail.html', {'post': post})


def category_posts(request, category_slug):
    category = get_object_or_404(
        Category,
        slug=category_slug,
        is_published=True
    )
    post_list = get_base_queryset().filter(
        category=category
    ).order_by('-pub_date')
    return render(
        request,
        'blog/category.html',
        {
            'category': category,
            'post_list': post_list
        }
    )
