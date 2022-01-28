from django import forms
from inventory.models import *

class laptopform(forms.ModelForm):
    class Meta:
        model=laptop
        fields=('type','price','status','issues')

class desktopform(forms.ModelForm):
    class Meta:
        model=desktop
        fields=('type','price','status','issues')

class mobileform(forms.ModelForm):
    class Meta:
        model=mobile
        fields=('type','price','status','issues')