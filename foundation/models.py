from django.db import models

from django.contrib.auth.models import User


class Post(models.Model):
	title = models.CharField(max_length=25, verbose_name='Название')
	descriptoinos = models.TextField(blank=True, verbose_name='Описание')
	created = models.DateTimeField(auto_now_add=True)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	liks = models.IntegerField(default=0, verbose_name='Лайки')
	col_comment = models.IntegerField(default=0, verbose_name='Количество коментариев')

	def __str__(self):
		return self.title


class Comment(models.Model):
	post_comment = models.ForeignKey(Post, on_delete=models.CASCADE)
	text = models.TextField(verbose_name='Коментарий')
	created = models.DateTimeField(auto_now_add=True)
	user = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return self.text


class UserProfile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	avatar = models.ImageField(upload_to='avatar', verbose_name='Изображение')
	status = models.CharField(max_length=100, blank=True, verbose_name='Статус')

	def __unicode__(self):
		return self.user