from django import forms


class ChangeEmailForm(forms.Form):
    email = forms.EmailField()


class ChangePhotoForm(forms.Form):
    photo = forms.URLField(max_length=100)
