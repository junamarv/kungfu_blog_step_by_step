from django import forms
from mypost.models import Post


class ListForm(forms.ModelForm):
	class Meta:
		model = Post
		exclude = [""]