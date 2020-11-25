from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user


class SubjectInput(forms.Form):
    subjectName1 = forms.CharField(max_length=50,widget=forms.TextInput(attrs={'placeholder': 'Subject'}))
    subject1Input1 = forms.FloatField(label='',max_value=100,min_value=0,widget=forms.NumberInput(attrs={'placeholder': 'Exam 1'}))
    subject1Input2 = forms.FloatField(label='',max_value=100,min_value=0,widget=forms.NumberInput(attrs={'placeholder': 'Exam 2'}))
    subject1Input3 = forms.FloatField(label='',max_value=100,min_value=0,widget=forms.NumberInput(attrs={'placeholder': 'Exam 3'}))
    subject1Input4 = forms.FloatField(label='',max_value=100,min_value=0,widget=forms.NumberInput(attrs={'placeholder': 'Exam 4'}))
    subject1Input5 = forms.FloatField(label='',max_value=100,min_value=0,widget=forms.NumberInput(attrs={'placeholder': 'Exam 5'}))
    subjectName2 = forms.CharField(max_length=50,widget=forms.TextInput(attrs={'placeholder': 'Subject'}))
    subject2Input1 = forms.FloatField(label='',max_value=100,min_value=0,widget=forms.NumberInput(attrs={'placeholder': 'Exam 1'}))
    subject2Input2 = forms.FloatField(label='',max_value=100,min_value=0,widget=forms.NumberInput(attrs={'placeholder': 'Exam 2'}))
    subject2Input3 = forms.FloatField(label='',max_value=100,min_value=0,widget=forms.NumberInput(attrs={'placeholder': 'Exam 3'}))
    subject2Input4 = forms.FloatField(label='',max_value=100,min_value=0,widget=forms.NumberInput(attrs={'placeholder': 'Exam 4'}))
    subject2Input5 = forms.FloatField(label='',max_value=100,min_value=0,widget=forms.NumberInput(attrs={'placeholder': 'Exam 5'}))
    subjectName3 = forms.CharField(max_length=50,widget=forms.TextInput(attrs={'placeholder': 'Subject'}))
    subject3Input1 = forms.FloatField(label='',max_value=100,min_value=0,widget=forms.NumberInput(attrs={'placeholder': 'Exam 1'}))
    subject3Input2 = forms.FloatField(label='',max_value=100,min_value=0,widget=forms.NumberInput(attrs={'placeholder': 'Exam 2'}))
    subject3Input3 = forms.FloatField(label='',max_value=100,min_value=0,widget=forms.NumberInput(attrs={'placeholder': 'Exam 3'}))
    subject3Input4 = forms.FloatField(label='',max_value=100,min_value=0,widget=forms.NumberInput(attrs={'placeholder': 'Exam 4'}))
    subject3Input5 = forms.FloatField(label='',max_value=100,min_value=0,widget=forms.NumberInput(attrs={'placeholder': 'Exam 5'}))
    subjectName4 = forms.CharField(max_length=50,widget=forms.TextInput(attrs={'placeholder': 'Subject'}))
    subject4Input1 = forms.FloatField(label='',max_value=100,min_value=0,widget=forms.NumberInput(attrs={'placeholder': 'Exam 1'}))
    subject4Input2 = forms.FloatField(label='',max_value=100,min_value=0,widget=forms.NumberInput(attrs={'placeholder': 'Exam 2'}))
    subject4Input3 = forms.FloatField(label='',max_value=100,min_value=0,widget=forms.NumberInput(attrs={'placeholder': 'Exam 3'}))
    subject4Input4 = forms.FloatField(label='',max_value=100,min_value=0,widget=forms.NumberInput(attrs={'placeholder': 'Exam 4'}))
    subject4Input5 = forms.FloatField(label='',max_value=100,min_value=0,widget=forms.NumberInput(attrs={'placeholder': 'Exam 5'}))
    subjectName5 = forms.CharField(max_length=50,widget=forms.TextInput(attrs={'placeholder': 'Subject'}))
    subject5Input1 = forms.FloatField(label='',max_value=100,min_value=0,widget=forms.NumberInput(attrs={'placeholder': 'Exam 1'}))
    subject5Input2 = forms.FloatField(label='',max_value=100,min_value=0,widget=forms.NumberInput(attrs={'placeholder': 'Exam 2'}))
    subject5Input3 = forms.FloatField(label='',max_value=100,min_value=0,widget=forms.NumberInput(attrs={'placeholder': 'Exam 3'}))
    subject5Input4 = forms.FloatField(label='',max_value=100,min_value=0,widget=forms.NumberInput(attrs={'placeholder': 'Exam 4'}))
    subject5Input5 = forms.FloatField(label='',max_value=100,min_value=0,widget=forms.NumberInput(attrs={'placeholder': 'Exam 5'}))