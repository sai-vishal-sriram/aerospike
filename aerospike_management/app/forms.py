from django import forms

class BackupForm(forms.Form):
    namespace = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Namespace",
                "class": "form-control"
            }
        ))

    dest_ntk_addr = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Destination Network Address",
                "class": "form-control"
            }
        ))

    srcfilesys = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Source File System",
                "class": "form-control"
            }
        ))

    ssh_username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "SSH User Name",
                "class": "form-control"
            }
        ))

    ssh_password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "SSH Password",
                "class": "form-control"
            }
        ))