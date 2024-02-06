from django import forms
from django.contrib.auth.models import User

class CustomSignUpForm(forms.Form):
    email = forms.EmailField(
        max_length=200, 
        help_text="Enter the email id",
        widget=forms.TextInput(attrs={'placeholder': 'Enter your email id'})
        )
    password = forms.CharField(
        label='Password',
        help_text="Enter the Password",
        widget=forms.PasswordInput(attrs={'placeholder': 'Password'}),
        
    )
    confirm_password = forms.CharField(
        label='Confirm Password',
        help_text="Confirm Password",
        widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password'})
    )

    def clean_username(self):
            email = self.cleaned_data['email']
            if User.objects.filter(email=email).exists():
                raise forms.ValidationError("This username is already taken. Please choose a different one.")
            return email

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password != confirm_password:
            raise forms.ValidationError("Passwords do not match")

    def save(self):
        email = self.cleaned_data['email']
        password = self.cleaned_data['password']
        user = User.objects.create_user(username=email, email=email, password=password)
        return user
