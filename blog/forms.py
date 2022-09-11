
from logging import PlaceHolder
from multiprocessing.sharedctypes import Value
from django import forms
from .models import Post,Category,Profile,Comment
from django.contrib.auth.forms import UserCreationForm,UserChangeForm,PasswordChangeForm
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model


choices=Category.objects.all().values_list('name','name')
choice_list=[]

for item in choices:
    choice_list.append(item)

class PostForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=('title','title_tag','author','category','body','header_image')

        widgets={
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'title_tag':forms.TextInput(attrs={'class':'form-control'}),
            'author':forms.TextInput(attrs={'class':'form-control','value':'','id':'elder','type':'hidden'}),
            #'author':forms.Select(attrs={'class':'form-control'}),
            'category':forms.Select(choices=choice_list,attrs={'class':'form-control'}),
            'body':forms.Textarea(attrs={'class':'form-control'}),
           
        }

class PostForm1(forms.ModelForm):
    class Meta:
        model=Post
        fields=('author','body')

        widgets={
           'author':forms.TextInput(attrs={'class':'form-control','value':'','id':'elder','type':'hidden'}),
            
            'body':forms.Textarea(attrs={'class':'form-control'}),
           
        }



class EditForm(forms.ModelForm):
    class Meta:
        
        model=Post
        fields=('title','title_tag','body')

        widgets={
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'title_tag':forms.TextInput(attrs={'class':'form-control'}),
            'body':forms.Textarea(attrs={'class':'form-control'}),
           
        }

class EditForm1(forms.ModelForm):
    class Meta:
        
        model=Post
        fields=('body',)

        widgets={
            
            'body':forms.Textarea(attrs={'class':'form-control'}),
           
        }






        
class EditProfileForm(UserChangeForm):
    email= forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    first_name=forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name=forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}))
    username=forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}))
  
   
    

    class Meta:
        model= User
        fields=('username','first_name','last_name','email')

class PasswordChangingForm(PasswordChangeForm):
    old_password= forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control', 'type':'password'}))
    new_password1=forms.CharField(max_length=100,widget=forms.PasswordInput(attrs={'class':'form-control', 'type':'password', 'placeHolder':'password'}))
    new_password2=forms.CharField(max_length=100,widget=forms.PasswordInput(attrs={'class':'form-control', 'type':'password', 'placeHolder':'comfirm password'}))
    

    class Meta:
        model= User
        fields=('old_password','new_password1')


class ProfilePageform(forms.ModelForm):
    class Meta:
        model=Profile
        fields=('bio','profile_pic','website_url','facebook_url','twitter_url','instagram_url')

        widgets={
            'bio':forms.Textarea(attrs={'class':'form-control'}),
            #'profile_pic':forms.TextInput(attrs={'class':'form-control'}),
            'website_url':forms.TextInput(attrs={'class':'form-control'}),
            'facebook_url':forms.TextInput(attrs={'class':'form-control'}),
            'twitter_url':forms.TextInput(attrs={'class':'form-control'}),
            'instagram_url':forms.TextInput(attrs={'class':'form-control'}),
         }


class ProfileEditform(forms.ModelForm):
    class Meta:
        model=Profile
        fields=('bio','profile_pic','website_url','facebook_url','twitter_url','instagram_url')

        widgets={
            'bio':forms.Textarea(attrs={'class':'form-control'}),
            #'profile_pic':forms.TextInput(attrs={'class':'form-control'}),
            'website_url':forms.TextInput(attrs={'class':'form-control'}),
            'facebook_url':forms.TextInput(attrs={'class':'form-control'}),
            'twitter_url':forms.TextInput(attrs={'class':'form-control'}),
            'instagram_url':forms.TextInput(attrs={'class':'form-control'}),
         }




class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields=('name','body')

        widgets={
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'body':forms.Textarea(attrs={'class':'form-control'}),
           
        }

class CommentForm1(forms.ModelForm):
    class Meta:
        model=Comment
        fields=('body',)

        widgets={
            
            'body':forms.Textarea(attrs={'class':'form-control'}),
           
        }




class SignUpForm(UserCreationForm):

    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        kwargs.setdefault('label_suffix', '')
        super().__init__(*args, **kwargs)
        self.fields['username'].label = "Username"
        self.fields['email'].label = "Email"
        self.fields['password1'].label = "Password"
        self.fields['password2'].label = "Comfirm Password"
        self.fields['username'].widget.attrs.update(
            {'class': 'myfieldclass form-control'})
        self.fields['email'].widget.attrs.update(
            {'class': 'myfieldclass form-control'})
        self.fields['password1'].widget.attrs.update(
            {'class': 'myfieldclass form-control'})
        self.fields['password2'].widget.attrs.update(
            {'class': 'myfieldclass form-control'})

        # giving place holders to fields
        self.fields['username'].widget.attrs.update(
            {'placeholder': 'Enter Your Username*'})
        self.fields['email'].widget.attrs.update(
            {'placeholder': 'Enter Your Email*'})
        self.fields['password1'].widget.attrs.update(
            {'placeholder': 'Password'})
        self.fields['password2'].widget.attrs.update(
            {'placeholder': 'Confirm Password'})

        for text in ['username', 'password1', 'password2']:
            self.fields[text].help_text = None



    




