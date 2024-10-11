from django import forms

from music_app.profiles.models import Profile


class CreateProfileForm(forms.ModelForm):
    class Meta:

        model = Profile
        fields = "__all__"
        # fields = ("username", "email", "age")

        widgets = {
            "username": forms.TextInput(attrs={'placeholder': 'Username'}),
            "email": forms.EmailInput(attrs={'placeholder': 'Email'}),
            "age": forms.NumberInput(attrs={'placeholder': 'Age'}),
        }


