from django import forms


from app_pages import models

class ContactForm(forms.ModelForm):
    class Meta:
        model = models.ContactModel
        fields = "__all__"