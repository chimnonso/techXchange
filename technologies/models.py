from django.db import models
from django.utils.translation import ugettext_lazy as _
from datetime import datetime
from django.contrib.auth import get_user_model

User = get_user_model()


class Technology(models.Model):
    name = models.CharField("Technology Name", max_length=150)
    company = models.CharField("Company Name", max_length=150)
    phone = models.CharField("Phone", max_length=15)
    company_address = models.CharField(_("Company Address"), max_length=50)
    short_description = models.CharField("Short details", max_length=250)
    description = models.TextField("Description")
    posted_by = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    
    date_posted = models.DateTimeField("Date Posted", default=datetime.now)
    upvotes = models.IntegerField(default=0)
    main_photo = models.ImageField("Upload Image", upload_to='photo/%Y/%m/%d', height_field=None, width_field=None, max_length=None)

    class Meta:
        ordering = ('-date_posted',)

    def __repr__(self):
        return f"<Technology {self.name}>"

    def __str__(self):
        return f"{self.name}"

class Contact(models.Model):
    name = models.CharField("Name", max_length=150)
    company = models.CharField("Company Name", max_length=150)
    email = models.EmailField("Email")
    phone = models.CharField("Phone", max_length=15)
    message = models.TextField("Message")
    
    technology = models.ForeignKey(Technology, on_delete=models.DO_NOTHING)
    # date_requested = models.DateTimeField("Date Requested", default=datetime.now, blank=True)

    def __repr__(self):
        return f"<Request by {self.name} on {self.technology.name} technology>"