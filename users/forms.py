from django import forms
from datetime import datetime
from django.contrib.auth.forms import UserCreationForm
from .models import User, CHOICE_GENDER, CHOICE_EDU

class RegisterForm(UserCreationForm):
    # age = forms.PositiveIntegerField(null=True, blank=True)
    # birth = forms.DateField(label="生日",default=datetime.now().date(),)
    sex = forms.ChoiceField(choices=CHOICE_GENDER, label="性别")
    # hobbies = forms.CharField(max_length=100, blank=True)
    education = forms.ChoiceField(choices=CHOICE_EDU, label="学历")
    # school = forms.CharField(max_length=20, blank=True)
    # introduction = forms.CharField(max_length=200, blank=True)
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username", "email", "sex", "birth", "education")

    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        user.birth = self.cleaned_data['birth']
        user.sex = self.cleaned_data['sex']
        user.education = self.cleaned_data['education']
        # user.age = date()-user.birth
        if commit:
            user.save()
        return user

# class AddInfoForm(UserCreationForm):
#     class Meta(forms.Form):
#         age = forms.PositiveIntegerField(null=True, blank=True)
#         sex = forms.ChoiceField(choices=CHOICE_GENDER)
#         hobbies = forms.CharField(max_length=100, blank=True)
#         education = forms.CharField(max_length=10, blank=True)
#         school = forms.CharField(max_length=20, blank=True)
#         introduction = forms.CharField(max_length=200, blank=True)
#         fields = ("username", "email", "age", "sex", "hobbies", "education", "school", "introduction")

class UploadImageForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["image"]