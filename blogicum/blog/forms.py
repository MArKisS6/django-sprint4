from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

from .models import Comment, Post

User = get_user_model()


class PostForm(forms.ModelForm):
    """Форма создания и редактирования публикации."""

    pub_date = forms.DateTimeField(
        widget=forms.DateTimeInput(
            attrs={'type': 'datetime-local'},
            format='%Y-%m-%dT%H:%M',
        ),
        input_formats=['%Y-%m-%dT%H:%M'],
        label='Дата и время публикации',
    )

    class Meta:
        model = Post
        fields = (
            'title', 'text', 'pub_date',
            'location', 'category', 'image',
        )


class CommentForm(forms.ModelForm):
    """Форма добавления и редактирования комментария."""

    class Meta:
        model = Comment
        fields = ('text',)


class CustomUserCreationForm(UserCreationForm):
    """Форма регистрации с расширенным набором полей."""

    class Meta:
        model = User
        fields = (
            'username', 'first_name', 'last_name', 'email',
        )


class ProfileEditForm(forms.ModelForm):
    """Форма редактирования профиля пользователя."""

    class Meta:
        model = User
        fields = (
            'username', 'first_name', 'last_name', 'email',
        )
