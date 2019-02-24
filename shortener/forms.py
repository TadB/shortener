from django import forms

from shortener.models import Link


class SetUrlForm(forms.ModelForm):
    class Meta:
        model = Link
        fields = ['full_url']
