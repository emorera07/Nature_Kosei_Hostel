from django import forms
from django.contrib import admin
from django.contrib.auth.models import Group
from users.models import User
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm 

class RegisterForm(UserCreationForm):
    username = forms.CharField(label = 'Nombre de Usuario') 
    email = forms.EmailField(label = 'email')
    #is_staff = forms.BooleanField(label = 'is_staff',required=False)

    class Meta: 
        model = User
        fields = ('username', 'email',)
        

    def save(self, commit=True):
        User = None 
        User = super(RegisterForm, self).save(commit=False) 
        User.email = self.cleaned_data['email']
        User.is_staff = False #self.cleaned_data['is_staff']
        if commit: 
            User.save() 
        return User 


class RegisterStaffForm(UserCreationForm):
    username = forms.CharField(label = 'Nombre de Usuario') 
    email = forms.EmailField(label = 'email')
    is_staff = forms.BooleanField(label = 'is_staff',required=False)

    class Meta: 
        model = User
        fields = ('username', 'email','is_staff')
        

    def save(self, commit=True):
        User = None 
        User = super(RegisterStaffForm, self).save(commit=False) 
        User.email = self.cleaned_data['email']
        User.is_staff = self.cleaned_data['is_staff']
        if commit: 
            User.save() 
        return User 

# Now register the new UserAdmin...
#admin.site.unregister(User)
#admin.site.unregister(admin)

admin.site.register(User)
#admin.site.register(User,UserAdmin)

#admin.site.register(User, UserAdmin)
# ... and, since we're not using Django's built-in permissions,
# unregister the Group model from admin.
#admin.site.unregister(Group)