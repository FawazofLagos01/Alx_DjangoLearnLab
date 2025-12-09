from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
from .models import Post
from .models import Comment
from .models import Tag

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Write your comment here...'}),
        }
        labels = {
            'content': '',
        }
        
class PostForm(forms.ModelForm):
    tags = forms.CharField(required=False, help_text='Enter tags separated by commas.')
  
    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Post Title'}),
            'content': forms.Textarea(attrs={'rows': 10, 'placeholder': 'Write your post here...'}),
        }

    def __init__(self, *args, **kwargs):
        instance = kwargs.get('instance', None)
        super().__init__(*args, **kwargs)
        if instance:
            tag_names = ', '.join([tag.name for tag in instance.tags.all()])
            self.fields['tags'].initial = tag_names
    
    def save(self, commit=True):
        instance = super().save(commit=False)
        if commit:
            instance.save()

        tags_str = self.cleaned_data.get('tags', '')
        tag_names = [t.strip() for t in tags_str.split(',') if t.strip()]
        new_tags = []
        for name in tag_names:
            tag_obj, _ = Tag.objects.get_or_create(name_iexact=False, name=name)
            new_tags.append(tag_obj)

        instance.tags.set(new_tags)
        return instance
    
class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True, help_text='Required. Enter a valid email address.')

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'avatar']