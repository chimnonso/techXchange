from django.forms import ModelForm, ValidationError
from .models import *


class TechnologyForm(ModelForm):
    
    class Meta:
        model = Technology
        exclude = ['posted_by', 'date_posted', 'upvotes']

        def clean_file(self):

            file = self.cleaned_data['file']

            try:
                main, sub = file.content_type.split('/')
                if not (main == 'image' and sub in ['jpeg', 'png'] ):
                    raise ValidationError(u"Please upload only JPEG or PNG")

                if len(file) > (10000 * 1024):
                    raise ValidationError(u"File size should be less than 10M")

            except AttributeError:
                pass
            
            return file

class ContactForm(ModelForm):

    class Meta:
        model = Contact
        exclude = ['technology']

    # def clean(self):
    #     super().clean()
    #     name = self.cleaned_data.get("name")
    #     email = self.cleaned_data.get("email")

    #     if not name:
    #         # msg = "Please give us your name"
    #         # self.add_error('name', msg)
    #         raise ValidationError("Please give us your name")
        
    #     if not email:
    #         # email_msg = "Please provide a valid mail"
    #         # self.add_error("email", email_msg)
    #         raise ValidationError("Please provide a valid mail")