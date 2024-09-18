from django import forms
from .models import Post


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        field = "__all__"
        exclude=('created_by', 'updated_by', 'deleted_by', 'created_at', 'updated_at', 'deleted_at', 'uuid')
        widgets= {
            "title" : forms.TextInput(attrs={"class":"py-3 px-4 block w-full border-gray-200 rounded-lg text-sm focus:border-blue-500 focus:ring-blue-500 disabled:opacity-50 disabled:pointer-events-none "}),
            "slug": forms.TextInput(attrs={"class":"py-3 px-4 block w-full border-gray-200 rounded-lg text-sm focus:border-blue-500 focus:ring-blue-500 disabled:opacity-50 disabled:pointer-events-none "}),
            "body": forms.Textarea(attrs={"class":"py-3 px-4 block w-full border-gray-200 rounded-lg text-sm focus:border-blue-500 focus:ring-blue-500 disabled:opacity-50 disabled:pointer-events-none ", "rows": "3"}),
        }


class EmailPostForm(forms.Form):
    name = forms.CharField(max_length=25)
    email = forms.EmailField()
    to = forms.EmailField()
    comments = forms.CharField(
        required=False,
        widget=forms.Textarea
    )