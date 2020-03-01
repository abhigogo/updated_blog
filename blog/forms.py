from django import forms
from django.contrib.auth.models import User
from blog.models import user_profile, Post, comment

class user_form(forms.ModelForm):

    class Meta:
        model = User
        fields = ('username','email','password')

        widgets = {
            'username':forms.TextInput(attrs={"class":"form-control",
                                              'placeholder':'Enter Username.....'}),
            'email':forms.TextInput(attrs={"class":"form-control",
                                           'placeholder':'Enter Email.....'}),
            'password':forms.PasswordInput(attrs={"class":"form-control",
                                              "placeholder":"Enter Password....."}),
        }

class profile_form(forms.ModelForm):

    class Meta:
        model = user_profile
        fields = ('profile_image',)

class post_form(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','text','image',)

        widgets = {
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'text':forms.Textarea(attrs={'class':'form-control'}),
        }
class comment_form(forms.ModelForm):
    class Meta:
        model = comment
        fields = ('name','text')

        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control',
                                          'id':'name_id'}),
            'text':forms.Textarea(attrs={'class':'form-control',
                                         'id':'text_id'})
        }

