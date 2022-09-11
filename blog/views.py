from contextlib import redirect_stderr
from multiprocessing import context
from django.shortcuts import render,get_object_or_404,redirect
from .models import Post,Category,Profile,Comment
from .forms import PostForm,PasswordChangingForm, PostForm,PostForm1,EditForm,EditProfileForm,ProfilePageform,CommentForm,SignUpForm,ProfileEditform,EditForm1,CommentForm1
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.contrib.auth.forms import UserCreationForm,UserChangeForm,PasswordChangeForm
from django.urls import reverse_lazy,reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.views import PasswordChangeView
from django.contrib import messages
from django.contrib.auth import get_user_model
User = get_user_model()
# Create your views here.





def CategoryView(request,cats):
    category_post=Post.objects.filter(category=cats.replace('-',' '))
    return render(request,'category.html',{'cats':cats.title().replace('-',' '),'category_post':category_post})


def CategoryListView(request):
    cat_menu_list=Category.objects.all()
    return render(request,'category_list.html',{'cat_menu_list':cat_menu_list})



class UserRegisterView(CreateView):
    form_class=SignUpForm
    template_name='register.html'
    success_url=reverse_lazy('home')




def LikeView(request, pk):
    post=get_object_or_404(Post, id=request.POST.get('post_id'))
    
    liked=False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user.id)
        liked=False
    else:
        post.likes.add(request.user.id)
        liked=True

    #return redirect (reverse('home', post.pk) + '#{{post.pk}}')
    #return HttpResponseRedirect(reverse('article-detail', args=[post.pk])+ '#{{post.pk}}')
    return redirect('home')


def FollowerView(request, pk):
    post=get_object_or_404(Post, id=request.POST.get('follow_id'))
    
    followed=False
    if post.followers.filter(id=request.user.id).exists():
        post.followers.remove(request.user.id)
        followed=False
    else:
        post.followers.add(request.user.id)
        followed=True

    #return redirect (reverse('home', post.pk) + '#{{post.pk}}')
    #return HttpResponseRedirect(reverse('article-detail', args=[post.pk])+ '#{{post.pk}}')
    return redirect('home')




class HomeView(ListView):
    model=Post
    template_name='home.html'
    ordering=['-id']

    def get_context_data(self, *args, **kwargs):
        cat_menu=Category.objects.all()
        context=super(HomeView, self).get_context_data(*args,**kwargs)
        context['cat_menu']= cat_menu
        return context

    

class ArticleDetailView(DetailView):
    model=Post
    template_name='article_details.html'

    def get_context_data(self, *args, **kwargs):
        cat_menu=Category.objects.all()
        context=super(ArticleDetailView, self).get_context_data(*args,**kwargs)
        
        stuff=get_object_or_404(Post, id=self.kwargs['pk'])
        total_likes=stuff.total_likes()

        liked=False
        if stuff.likes.filter(id=self.request.user.id).exists():
            liked=True

        context['cat_menu']= cat_menu
        context['total_likes']= total_likes
        context['liked']=liked
        return context


class AddPostView(CreateView):
    model=Post
    form_class=PostForm
    template_name="add_post.html"
    #fields='__all__'

class AddPostView1(CreateView):
    model=Post
    form_class=PostForm1
    template_name="add_post1.html"
    #fields='__all__'

class UpdatePostView(UpdateView):
    model=Post
    form_class=EditForm
    template_name="update_post.html"
    #fields=['title','title_tag','body']

class UpdateQuestionView(UpdateView):
    model=Post
    form_class=EditForm1
    template_name="update_question.html"
    #fields=['title','title_tag','body']

class DeletePostView(DeleteView):
    model=Post
    template_name="delete_post.html"
    success_url=reverse_lazy('home')

class PasswordsChangeView(PasswordChangeView):
    form_class=PasswordChangingForm
    success_url=reverse_lazy('password-success')
    #success_url=reverse_lazy('home')

def password_success(request):
    return render(request,'password_success.html')


class UserEditView(UpdateView):
    form_class=EditProfileForm
    template_name='edit_profile.html'
    success_url=reverse_lazy('home')

    def get_object(self):
        return self.request.user



class ShowProfilePageView(DetailView):
    model=Profile
    template_name='user_profile.html'

    def get_context_data(self, *args, **kwargs):
        users=Profile.objects.all()
        context=super(ShowProfilePageView, self).get_context_data(*args,**kwargs)

        page_user= get_object_or_404(Profile, id=self.kwargs['pk'])
        context['page_user']= page_user
        return context


class EditProfilePageView(UpdateView):
    model=Profile
    template_name='edit_profile_page.html'
    #fields=ProfileEditform
    fields=['bio','profile_pic','website_url','facebook_url','twitter_url','instagram_url']
    success_url=reverse_lazy('home')

class CreateProfilePageView(CreateView):
    model=Profile
    form_class=ProfilePageform
    template_name='create_user_page.html'
    #fields=('bio','profile_pic','website_url','facebook_url','twitter_url','instagram_url')

    def form_valid(self, form):
        form.instance.user=self.request.user
        return super().form_valid(form)



class AddCommentView(CreateView):
    model=Comment
    form_class=CommentForm
    template_name="add_comment.html"
    #fields='__all__'
    def form_valid(self, form):
        form.instance.post_id=self.kwargs['pk']
        return super().form_valid(form)
    success_url=reverse_lazy('home')


class AddCommentView1(CreateView):
    model=Comment
    form_class=CommentForm1
    template_name="add_comment1.html"
    #fields='__all__'
    def form_valid(self, form):
        form.instance.post_id=self.kwargs['pk']
        return super().form_valid(form)
    success_url=reverse_lazy('home')