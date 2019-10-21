from django import forms
from .models import File


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
        if file._size > settings.MAX_UPLOAD_SIZE:
            raise forms.ValidationError(_('文件大小不得超过 % s 哦') % (
                filesizeformat(settings.MAX_UPLOAD_SIZE)))
        return file
