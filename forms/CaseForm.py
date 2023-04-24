from django import forms
from dashboard.models import Case


class CaseForm(forms.ModelForm):
    title = forms.CharField(
        label='Title',
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'input input-bordered w-full max-w-full',
                'placeholder': 'murder mistery',
                'autocomplete': 'off'
            }
        ),
    )

    class Meta:
        model = Case
        fields = (
            'title',
        )

    def clean(self):
        super(CaseForm, self).clean()

        title = self.cleaned_data.get('title')

        if not title:
            self._errors['title'] = self.error_class([
                'Please provide valid title'])
            self.fields['title'].widget.attrs.update({'class': 'input-error input input-bordered w-full max-w-full'})

        return self.cleaned_data
