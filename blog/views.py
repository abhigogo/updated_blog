from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import (TemplateView,ListView,
                                  CreateView, UpdateView,
                                  DetailView, DeleteView)
from .forms import user_form, profile_form, post_form, comment_form
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.urls import reverse, reverse_lazy
from .models import Post, comment
from django.utils import timezone
from rest_framework import viewsets
from .serializers import PostSerializer
# Create your views here.

class base(TemplateView):
    template_name = 'blog/index.html'

def registration(request):
    registered = False
    if request.method == 'POST':
        userform = user_form(data=request.POST)
        profileform = profile_form(data=request.POST)
        if userform.is_valid() and profileform.is_valid():
            user = userform.save()
            user.set_password(user.password)
            user.save()
            profile = profileform.save(commit=False)
            profile.user = user
            if 'profile_image' in request.FILES:
                profile.profile_image = request.FILES['profile_image']
            profile.save()
            return redirect('base')
        else:
            print(userform.errors,profileform.errors)
    else:
        userform = user_form()
        profileform = profile_form()

    return render(request,'registration/register.html',{'userform':userform,
                                                        'profileform':profileform,
                                                        'registered':registered})

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username,password=password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('postlist'))
            else:
                return HttpResponse("User is Not Active!")
        else:
            return HttpResponse("Invalid LogIn Credentials!")
    else:
        return render(request,'registration/login.html',{})

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('postlist'))

class postlist(ListView):
    model = Post

    def get_queryset(self):
        return Post.objects.filter(published_date__lte = timezone.now()).order_by('-published_date')

class postdetail(DetailView):
    model = Post

class draftlist(ListView):
    model = Post

    def get_queryset(self):
        return Post.objects.filter(published_date__isnull = True).order_by('created_date')

class postcreate(CreateView):
    model = Post
    form_class = post_form

    

class postupdate(UpdateView):
    model = Post
    fields = ('title','text')

class postdelete(DeleteView):
    model = Post
    success_url = reverse_lazy('postlist')

def publishpost(request,pk):
    post = get_object_or_404(Post,pk=pk)
    post.publish()
    return redirect('postlist')

def add_comment(request,pk):
    post = get_object_or_404(Post,pk=pk)
    if request.method == 'POST':
        form = comment_form(data=request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.Post = post
            comment.save()
            return redirect('postdetail',pk=post.pk)
    else:
        form = comment_form()
    return render(request,'blog/comment_form.html',{'form':form})

def approve_comment(request,pk):
    Comment = get_object_or_404(comment,pk=pk)
    Comment.approve_comment()
    return redirect('postdetail',pk=Comment.post.pk)

def delete_comment(request,pk):
    Comment = get_object_or_404(comment,pk=pk)
    post_pk = Comment.Post.pk
    Comment.delete()
    return redirect('postdetail',pk=post_pk)

class postview(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
