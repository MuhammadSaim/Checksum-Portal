from django import forms
from authentication.models import User


class LoginForm(forms.Form):
    username = forms.CharField(
        label='Username',
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'input input-bordered w-full max-w-full',
                'placeholder': 'jhon',
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

        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        user = User.objects.filter(username=username).first()

        if not username:
            self._errors['username'] = self.error_class([
                'Please provide valid username'])
            self.fields['username'].widget.attrs.update({'class': 'input-error input input-bordered w-full max-w-full'})

        if not password:
            self._errors['password'] = self.error_class([
                'Please provide password'])
            self.fields['password'].widget.attrs.update({'class': 'input-error input input-bordered w-full max-w-full'})

        if user is None:
            self._errors['username'] = self.error_class([
                'Sorry we can\'t found user with this username'])
            self.fields['username'].widget.attrs.update({'class': 'input-error input input-bordered w-full max-w-full'})

        if len(password) < 8:
            self._errors['password'] = self.error_class([
                'Password should be greater then 8 characters'])
            self.fields['password'].widget.attrs.update({'class': 'input-error input input-bordered w-full max-w-full'})

        return self.cleaned_data
