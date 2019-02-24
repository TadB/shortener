from django import forms

from shortener.models import Link


class SetUrlForm(forms.ModelForm):

    class Meta:
        model = Link
        labels = {"full_url": "Original URL"}
        fields = ['full_url']
