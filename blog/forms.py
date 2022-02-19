from django import forms
from .models import Blog,Comment

class BlogForm(forms.ModelForm):

    class Meta:
        model=Blog
        fields=("Title","Content","Image","Category","status",)
 
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields=('content',)
        widgets = {
            'content': forms.Textarea(attrs={'cols': 40, 'rows': 2}),
        }