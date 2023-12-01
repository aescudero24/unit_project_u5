from django import forms

# Create your forms here.


class CrimeSceneReportForm(forms.Form):
    date = forms.DateField(required=False)
    location = forms.CharField(required=False)
    officer = forms.CharField(required=False)
