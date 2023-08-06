from django import forms
from .models import Employee
# from .models import Employee, Granter, EmployeeLogin

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Username',
    }))
    password = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Password',
        'type': 'password'
    }))


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'
        widgets = {
            'admission_date': forms.DateInput(attrs={'class': 'form-control datepicker', 'required': True}),
            'father_name': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
            'id_number': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
            'name': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
            'mother_name': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
            'mobile_number': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
            'nid_number': forms.TextInput(attrs={'class': 'form-control'}),
            'husband_or_wife_name': forms.TextInput(attrs={'class': 'form-control'}),
            'salary': forms.NumberInput(attrs={'class': 'form-control', 'required': True}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'required': True}),
            'religion': forms.TextInput(attrs={'class': 'form-control'}),
            'note': forms.Textarea(attrs={'class': 'form-control'}),
            'second_contact_number': forms.TextInput(attrs={'class': 'form-control'}),
            # ImageField doesn't need a widget
        }





