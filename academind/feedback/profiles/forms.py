from django import forms


class ProfileFileForm(forms.Form):
  text = forms.FileField(allow_empty_file=True)
  image = forms.ImageField()