from django import forms
from authentication.models import User


class UserForm(forms.ModelForm):
    first_name = forms.CharField(
        label='First name',
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'input input-bordered w-full max-w-full',
                'placeholder': 'jhon',
                'autocomplete': 'off'
            }
        )
    )

    last_name = forms.CharField(
        label='Last name',
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'input input-bordered w-full max-w-full',
                'placeholder': 'Doe',
                'autocomplete': 'off'
            }
        )
    )

    username = forms.CharField(
        label='Username',
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'input input-bordered w-full max-w-full',
                'placeholder': 'jhon',
                'autocomplete': 'off'
            }
        )
    )

    email = forms.EmailField(
        label='Email',
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'input input-bordered w-full max-w-full',
                'placeholder': 'someone@example.com',
                'autocomplete': 'off'
            }
        )
    )

    password = forms.CharField(
        label='Password',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'class': 'input input-bordered w-full max-w-full',
                'autocomplete': 'off'
            }
        )
    )

    confirm_password = forms.CharField(
        label='Confirm password',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'class': 'input input-bordered w-full max-w-full',
                'autocomplete': 'off'
            }
        )
    )

    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'first_name',
            'last_name',
            'password',
            'confirm_password',
        )

    def clean(self):
        super(UserForm, self).clean()

        username = self.cleaned_data.get('username')
        email = self.cleaned_data.get('email')
        first_name = self.cleaned_data.get('first_name')
        last_name = self.cleaned_data.get('last_name')
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')

        email_qs = User.objects.filter(email=email)

        if email_qs.exists():
            self._errors['email'] = self.error_class([
                'This email is already exists.'])
            self.fields['email'].widget.attrs.update({'class': 'input-error input input-bordered w-full max-w-full'})

        if not password:
            self._errors['password'] = self.error_class([
                'Please provide the password'])
            self.fields['password'].widget.attrs.update({'class': 'input-error input input-bordered w-full max-w-full'})

        if len(password) < 8:
            self._errors['password'] = self.error_class([
                'Password should be greater then 8 characters'])
            self.fields['password'].widget.attrs.update({'class': 'input-error input input-bordered w-full max-w-full'})

        if not confirm_password:
            self._errors['confirm_password'] = self.error_class([
                'Please provide valid confirm password'])
            self.fields['confirm_password'].widget.attrs.update({'class': 'input-error input input-bordered w-full max-w-full'})

        if password != confirm_password:
            self._errors['password'] = self.error_class([
                'Password must be matched with confirm password.'])
            self.fields['password'].widget.attrs.update({'class': 'input-error input input-bordered w-full max-w-full'})

        return self.cleaned_data
