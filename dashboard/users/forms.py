from django import forms
from .models import Patient, Doctor, User

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'profile_picture', 'username', 'email', 'password', 'confirm_password', 'address_line1', 'city', 'state', 'pincode']

class PatientForm(UserForm):
    # Additional fields for patient if needed
    class Meta(UserForm.Meta):
        model = Patient

class DoctorForm(UserForm):
    # Additional fields for doctor if needed
    class Meta(UserForm.Meta):
        model = Doctor
