from django import forms
from authentication.models import User


class LoginForm(forms.Form):
    email = forms.CharField(
        label='Email',
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'input input-bordered w-full max-w-full',
                'placeholder': 'someone@example.com',
                'autocomplete': 'off'
            }
        ),
    )

    password = forms.CharField(
        label='Password',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'class': 'input input-bordered w-full max-w-full',
                'autocomplete': 'off'
            }
        ),
    )

    def clean(self):
        super(LoginForm, self).clean()

        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')

        user = User.objects.filter(email=email).first()

        if not email:
            self._errors['email'] = self.error_class([
                'Please provide valid email'])
            self.fields['email'].widget.attrs.update({'class': 'input-error input input-bordered w-full max-w-full'})

        if not password:
            self._errors['password'] = self.error_class([
                'Please provide password'])
            self.fields['password'].widget.attrs.update({'class': 'input-error input input-bordered w-full max-w-full'})

        if user is None:
            self._errors['email'] = self.error_class([
                'Sorry we can\'t found user with this email'])
            self.fields['email'].widget.attrs.update({'class': 'input-error input input-bordered w-full max-w-full'})

        if len(password) < 8:
            self._errors['password'] = self.error_class([
                'Password should be greater then 8 characters'])
            self.fields['password'].widget.attrs.update({'class': 'input-error input input-bordered w-full max-w-full'})

        return self.cleaned_data
