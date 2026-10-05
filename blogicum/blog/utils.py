from django.db.models import Count
from django.utils import timezone

from .models import Post


def get_posts(
    manager=Post.objects,
    published_only=False,
    with_comments=False
):
    """Возвращает QuerySet постов с select_related."""
    queryset = manager.select_related(
        'author', 'location', 'category'
    )
    if published_only:
        queryset = queryset.filter(
            is_published=True,
            pub_date__lte=timezone.now(),
            category__is_published=True
        )
    if with_comments:
        queryset = queryset.annotate(
            comment_count=Count('comments')
        ).order_by('-pub_date')
    return queryset
