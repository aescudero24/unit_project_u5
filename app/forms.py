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


class DriversLicenseForm(forms.Form):
    license_id = forms.IntegerField(required=False)
    age = forms.IntegerField(required=False)
    height = forms.IntegerField(required=False)
    hair_color = forms.CharField(required=False)
    gender = forms.CharField(required=False)


class LibraryCardForm(forms.Form):
    aisle = forms.IntegerField(required=False)
    books = forms.IntegerField(required=False)


class InterviewForm(forms.Form):
    personal_id = forms.IntegerField(required=False)


class SolveMysteryForm(forms.Form):
    personal_id = forms.IntegerField()
    full_name = forms.CharField()
