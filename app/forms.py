from django import forms

from django.core import validators
def validate_for_k(data):
    if data.lower().startswith('k'):
        raise forms.ValidationError('started with k')

def validate_forl_len(data):
    if len(data)<5:
        raise forms.ValidationError('len is < 5')

class SchoolForm(forms.Form):
    Sname=forms.CharField(validators=[validate_for_k,validators.MinLengthValidator(4)])
    Sprincipal=forms.CharField(validators=[validate_for_k])
    Slocation=forms.CharField()
    email=forms.EmailField()
    reenteremail=forms.EmailField()
    botcatcher=forms.CharField(required=False,widget=forms.HiddenInput)

    def clean_botcatcher(self):
        b=self.cleaned_data['botcatcher']
        if len(b)>0:
            raise forms.ValidationError('bot')

    def clean(self):
        e=self.cleaned_data['email']
        re=self.cleaned_data['reenteremail']
        if e!=re:
            raise forms.ValidationError('emails not matched')
    









    