from django import forms
from django.core.mail.message import EmailMessage
from django.utils.translation import gettext_lazy as _ 

class ContactForm(forms.Form):
    name = forms.CharField(label=_('Name'), max_length=100)
    email = forms.EmailField(label=_('E-mail'), max_length=100)
    subject = forms.CharField(label=_('Subject'), max_length=100)
    message = forms.CharField(label=_('Message'), widget=forms.Textarea())

    def send_email(self):
        name = self.cleaned_data['name']
        email = self.cleaned_data['email']
        subject = self.cleaned_data['subject']
        message = self.cleaned_data['message']
        
        n = _('Name')
        e = _('E-mail')
        s = _('Subject')
        m = _('Message')

        body = f'{n}: {name}\n{e}:{email}\n{s}: {subject}\n\
                    {m}: {message}'
        mail = EmailMessage(
            subject=subject,
            body=body,
            from_email='contato@fusion.com.br',
            to=['contato@fusion.com.br'],
            headers={'Reply-To': email}
        )
        mail.send()