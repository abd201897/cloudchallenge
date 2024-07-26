from django import forms

class MarsPhotoForm(forms.Form):
    photo_id = forms.IntegerField(label='Photo ID')
