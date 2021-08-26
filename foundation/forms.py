from django.forms import ModelForm
from .models import Post, Comment, UserProfile


class TrelloForms(ModelForm):

	class Meta:
		model = Post
		fields = ['title', 'descriptoinos']


class CommentForms(ModelForm):

	class Meta:
		model = Comment
		fields = ['text']


class UserProfileForms(ModelForm):

	class Meta:
		model = UserProfile
		fields = ['avatar', 'status']
