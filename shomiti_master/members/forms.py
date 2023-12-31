from .models import Granter
from django import forms
from .models import Employee, Granter, EmployeeLogin
from .models import Hotel
from django import forms

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
    admission_date = forms.DateField(
        widget=forms.DateInput(attrs={'class': 'form-control'})
    )
    father_name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    id_number = forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={'class': 'form-control'}),

    )
    name = forms.CharField(
        max_length=200,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    mother_name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    mobile_number = forms.CharField(
        max_length=20,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    nid_number = forms.CharField(
        max_length=20,
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        required=False
    )
    husband_or_wife_name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        required=False
    )
    salary = forms.DecimalField(
        max_digits=10,
        decimal_places=2,
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )
    address = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control'})
    )
    religion = forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    note = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control'}),
        required=False
    )
    second_contact_number = forms.CharField(
        max_length=20,
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        required=False
    )
    image = forms.ImageField(
        widget=forms.FileInput(attrs={'class': 'form-control-file'}),
        required=False
    )

    class Meta:
        model = Employee
        fields = '__all__'


class GranterForm(forms.ModelForm):
    class Meta:
        model = Granter
        fields = '__all__'

    name = forms.CharField(max_length=200, widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    father_name = forms.CharField(
        max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    mobile_number = forms.CharField(
        max_length=20, widget=forms.TextInput(attrs={'class': 'form-control'}))
    address = forms.CharField(widget=forms.Textarea(
        attrs={'class': 'form-control'}))
    husband_or_wife_name = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'class': 'form-control'}), required=False)
    shop = forms.CharField(max_length=200, widget=forms.TextInput(
        attrs={'class': 'form-control'}), required=False)
    religion = forms.CharField(
        max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    note = forms.CharField(widget=forms.Textarea(
        attrs={'class': 'form-control'}), required=False)
    second_contact_number = forms.CharField(
        max_length=20,
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        required=False
    )

    class Meta:
        model = Granter
        fields = '__all__'


class EmployeeLoginForm(forms.ModelForm):
    class Meta:
        model = EmployeeLogin
        fields = '__all__'

    user_name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        required=False
    )

    password = forms.CharField(
        max_length=128,
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        required=False
    )

    language = forms.ChoiceField(
        choices=EmployeeLogin.LANGUAGE_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'}),
        required=False
    )

    role = forms.ChoiceField(
        choices=EmployeeLogin.ROLE_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'}),
        required=False
    )

    login_permission = forms.ChoiceField(
        choices=EmployeeLogin.LOGIN_PERMISSION_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'}),
        required=False
    )

    employee = forms.ModelChoiceField(
        queryset=Employee.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'}),
        required=False
    )


class HotelForm(forms.ModelForm):

    class Meta:
        model = Hotel
        fields = ['name', 'hotel_Main_Img']
