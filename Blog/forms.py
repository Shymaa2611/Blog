from django import forms
from .models import Comment
class postForm(forms.Form):
    name=forms.CharField(max_length=20)
    email_from=forms.EmailField()
    email_to=forms.EmailField()
    comments = forms.CharField(required=False,widget=forms.Textarea)

class commentForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields=('name','email','content')
