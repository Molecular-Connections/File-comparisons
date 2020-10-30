
from django import forms

from . import models

class File_Upload_Form(forms.ModelForm):

    class Meta:

        model = models.File_Upload

        fields = ('title','file_1','file_2')

