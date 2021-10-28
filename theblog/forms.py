from django import forms
from .models import Post,Category

# choices=[('German','German'),('Japan','Japan'),('United Kingdom','United Kingdom'),('USA','USA')]
choices= Category.objects.all().values_list('name','name')

choices_l=[]

for item in choices:
  choices_l.append(item)


class PostForm(forms.ModelForm):
  class Meta:
    model = Post
    fields = ('title', 'author','category','images','body')

    widgets={
      'title': forms.TextInput(attrs={'class':'form-control'}),
      'author':forms.Select(attrs={'class':'form-control'}),
      'category':forms.Select(choices=choices_l,attrs={'class':'form-control'}),
      'body': forms.Textarea(attrs={'class':'form-control'})
    } 
    