from django import forms
from records.models import Post #, Newsletter
#from django.contrib.auth.models import User
from django.conf import settings

class PostForm(forms.ModelForm):
    post = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write the Name of the Document...'
        }
    ))
    document = forms.FileField()

    class Meta:
        model = Post
        fields = ('post','document')

    def save(self, user=None):
        post = super(PostForm, self).save(commit=True)
        #if User:
        #    post.User = user
        post.save()
        return post
