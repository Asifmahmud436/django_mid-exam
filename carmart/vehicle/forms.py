from django import forms
from .models import Vehicles,Comment


class VehicleForm(forms.ModelForm):
    class Meta:
        model = Vehicles
        fields = '__all__'


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name','email','body']