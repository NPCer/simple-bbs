from django import forms
from .models import File


# Model form
class FileUploadModelForm(forms.ModelForm):
    class Meta:
        model = File
        fields = ('file', 'upload_method',)

        widgets = {
            'upload_method': forms.TextInput(attrs={'class': 'form-control'}),
            'file': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }

    def clean_file(self):
        file = self.cleaned_data['file']
        ext = file.name.split('.')[-1].lower()
        if ext not in ["jpg", "pdf", "xlsx"]:
            raise forms.ValidationError(
                "Only jpg, pdf and xlsx files are allowed.")
        # return cleaned data is very important.
        return file
