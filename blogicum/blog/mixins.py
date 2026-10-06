from django.contrib.auth.mixins import UserPassesTestMixin
from django.shortcuts import redirect

from .models import Comment


class OnlyAuthorMixin(UserPassesTestMixin):
    """Миксин: доступ только автору объекта.

    Если текущий пользователь не является автором,
    выполняется редирект на страницу просмотра объекта.
    """

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

    def handle_no_permission(self):
        return redirect(
            'blog:post_detail',
            post_id=self.kwargs['post_id']
        )


class CommentEditMixin:
    """Миксин: общие атрибуты для редактирования и удаления
    комментария.
    """

    model = Comment
    template_name = 'blog/comment.html'
    pk_url_kwarg = 'comment_id'
