from django import forms

# Create your forms here.


class CrimeSceneReportForm(forms.Form):
    date = forms.DateField(required=False)
    location = forms.CharField(required=False)
    officer = forms.CharField(required=False)


class SuspectForm(forms.Form):
    personal_id = forms.IntegerField(required=False)
    first_name = forms.CharField(required=False)
    last_name = forms.CharField(required=False)
    drivers_license_id = forms.IntegerField(required=False)
