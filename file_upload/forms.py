from django import forms
from .models import File
from django.template.defaultfilters import filesizeformat
from django.utils.translation import ugettext_lazy
from django.conf import settings


# Model form
class FileUploadModelForm(forms.ModelForm):
    class Meta:
        model = File
        fields = ('file', 'filename')

        widgets = {
            'filename': forms.TextInput(attrs={'class': 'form-control'}),
            'file': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }

    def clean_file(self):
        file = self.cleaned_data['file']
        ext = file.name.split('.')[-1].lower()
        if ext not in ["jpg", "pdf", "png", 'gif']:
            raise forms.ValidationError(
                "只能上传jpg pdf png gif文件")
        if file.size > settings.MAX_UPLOAD_SIZE:
            raise forms.ValidationError(('文件大小不得超过 % s 哦') % (
                filesizeformat(settings.MAX_UPLOAD_SIZE)))
        return file
