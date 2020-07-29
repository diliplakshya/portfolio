"""
Django forms for portfolio project
"""

from django import forms


class ContactForm(forms.Form):
    email        =   forms.EmailField(widget=forms.TextInput(
                                    attrs=
                                    {
                                        "placeholder" : "Enter your email address"
                                    }))
    subject         =   forms.CharField(max_length=50, 
                                widget=forms.TextInput(
                                    attrs=
                                    {
                                        "placeholder" : "Enter the Subject",
                                        "class" : "form-control-sm",
                                        "type" : "text"
                                    }
                                    ))
    message         =   forms.CharField(
                            widget=forms.Textarea(
                                attrs=
                                {"rows": 3, "cols":20, "class" : "form-control-sm", "placeholder" : "Enter the Message"}
                                ))