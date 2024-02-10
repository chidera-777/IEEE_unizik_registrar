from .models import UserRegistrar
from django import forms

class UserRegistrarForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['phoneNumber'].help_text = "Input your country code then your number. E.g \'+2348100000000\' "
    
    class Meta:
        model = UserRegistrar
        fields = ["email", "firstName", "lastName", "phoneNumber", "level", "societies", "IEEE_number"]
        
    def validate_email(self):
        email = self.cleaned_data.get("email")
        if UserRegistrar.objects.filter(email__iexact=email).exists():
            raise forms.ValidationError("A User with this email already exists!!!")
        return email