from django import forms
from django.contrib.auth.models import User
from .models import Task

TAILWIND_INPUT_CLASS = 'appearance-none rounded-lg relative block w-full px-3 py-2 border border-gray-300 dark:border-gray-600 placeholder-gray-500 dark:placeholder-gray-400 text-gray-900 dark:text-white dark:bg-gray-700 focus:outline-none focus:ring-2 focus:ring-primary focus:border-transparent sm:text-sm transition-colors'

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': TAILWIND_INPUT_CLASS, 'placeholder': 'Password'}))
    password_confirm = forms.CharField(widget=forms.PasswordInput(attrs={'class': TAILWIND_INPUT_CLASS, 'placeholder': 'Confirm Password'}), label='Confirm Password')

    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        widgets = {
            'username': forms.TextInput(attrs={'class': TAILWIND_INPUT_CLASS, 'placeholder': 'Username'}),
            'email': forms.EmailInput(attrs={'class': TAILWIND_INPUT_CLASS, 'placeholder': 'Email address'}),
        }

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("This email is already in use.")
        return email

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password_confirm = cleaned_data.get('password_confirm')

        if password and password_confirm and password != password_confirm:
            raise forms.ValidationError("Passwords do not match.")
        return cleaned_data

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'category', 'priority', 'due_date']
        widgets = {
            'title': forms.TextInput(attrs={'class': TAILWIND_INPUT_CLASS, 'placeholder': 'Task title'}),
            'description': forms.Textarea(attrs={'class': TAILWIND_INPUT_CLASS, 'rows': 3, 'placeholder': 'Description (optional)'}),
            'category': forms.Select(attrs={'class': TAILWIND_INPUT_CLASS}),
            'priority': forms.Select(attrs={'class': TAILWIND_INPUT_CLASS}),
            'due_date': forms.DateInput(attrs={'class': TAILWIND_INPUT_CLASS, 'type': 'date'}),
        }
