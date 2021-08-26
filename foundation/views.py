from django.shortcuts import render, redirect, get_object_or_404

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required

from django.db import IntegrityError

from .models import Post, Comment

from .forms import TrelloForms, CommentForms, UserProfileForms


# user registration
def signup_user(request):
	if request.method == 'GET':
		return render(request, 'signup_user.html', {'form': UserCreationForm()})
	else:
		if request.POST['password1'] == request.POST['password2']:
			try:
				user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
				user.save()
				login(request, user)
				return redirect("home")
			except IntegrityError:
				return render(request, 'signup_user.html', {
					'form': UserCreationForm(),
					'error': 'Имя пользователя занято'
				})
		else:
			return render(request, 'signup_user.html', {
				'form': UserCreationForm(),
				'error': 'Пароль уже занят'
			})


# user authorization
def login_user(request):
	if request.method == 'GET':
		return render(request, 'login_user.html', {'form': AuthenticationForm()})
	else:
		user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
		if user is None:
			return render(request, 'login_user.html', {'form': AuthenticationForm(), 'error': 'Пользователь не найден'})
		else:
			login(request, user)
			return redirect("home")


@login_required
def posts_detail(request, id):
	posts_detail = get_object_or_404(Post, id=id)
	comments = Comment.objects.filter(post_comment=str(id)).order_by('-created')
	users = User.objects.filter(username=request.user)
	if request.method == 'GET':
		return render(request, 'posts.html', {
			'form': CommentForms(),
			'posts_detail': posts_detail,
			'comments': comments,
			'users': users
		})
	else:
		try:
			form = CommentForms(request.POST)
			posts_detail.col_comment += 1
			new_comment = form.save(commit=False)
			new_comment.post_comment = posts_detail
			new_comment.user = request.user
			posts_detail.save()
			new_comment.save()
			return redirect('posts_detail', id)
		except ValueError:
			return render(request, 'posts.html', {
				'form': CommentForms(),
				'posts_detail': posts_detail,
				'comments': comments,
				'users': users
			})


@login_required
def Home(request):
	# images user and name
	users = User.objects.filter(username=request.user)
	# post (title, descriptions, .....)
	posts = Post.objects.filter(user=request.user).order_by('-created')
	people = User.objects.all()
	if request.method == 'GET':
		return render(request, 'home.html', {'form': TrelloForms(), 'posts': posts, 'users': users, 'people': people})
	else:
		try:
			form = TrelloForms(request.POST)
			new_trello = form.save(commit=False)
			new_trello.user = request.user
			new_trello.save()
			return redirect('home')
		except ValueError:
			return render(request, 'home.html', {'form': TrelloForms(), 'posts': posts, 'users': users, 'people': people})


@login_required
def settingi(request):
	if request.method == 'GET':
		return render(request, 'settingi.html', {'form': UserProfileForms()})
	else:
		form = UserProfileForms(request.POST)
		new_trello = form.save(commit=False)
		new_trello.user = request.user
		new_trello.save()
		return redirect('settingi')


@login_required
def delete(request, id):
	post_delete = get_object_or_404(Post, id=id, user=request.user)
	post_delete.delete()
	return redirect('home')


@login_required
def like(id):
	post_delete = get_object_or_404(Post, id=id)
	post_delete.liks += 1
	post_delete.save()
	return redirect('home')


@login_required
def dislike(id):
	post_delete = get_object_or_404(Post, id=id)
	post_delete.liks -= 1
	post_delete.save()
	return redirect('home')


@login_required
def people_list(request):
	people = User.objects.all()
	return render(request, 'people_list.html', {'people': people})


@login_required
def people_detail(request, id):
	user = get_object_or_404(User, id=id)
	posts = Post.objects.filter(user=id).order_by('-created')
	return render(request, 'people_detail.html', {'user': user, 'posts': posts})


@login_required
def logout_user(request):
	logout(request)
	return redirect('login')
