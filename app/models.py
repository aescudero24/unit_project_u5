from django.db import models


# Create your models here.
class CrimeSceneReport(models.Model):
    date = models.DateField()
    location = models.TextField()
    officer = models.TextField()
    description = models.TextField()


def create_crime_scene_report(
    date,
    location,
    officer,
    description,
):
    report = CrimeSceneReport(
        date=date,
        location=location,
        officer=officer,
        description=description,
    )
    report.save()
    return report


def all_crime_scene_reports():
    return CrimeSceneReport.objects.all()


def find_crime_scene_reports(date=None, location=None, officer=None):
    try:
        reports = CrimeSceneReport.objects.all()
        if date:
            reports = reports.filter(date=date)
        if location:
            reports = reports.filter(location=location)
        if officer:
            reports = reports.filter(officer=officer)
        return reports  # Retrieve the first result or None if no matches
    except CrimeSceneReport.DoesNotExist:
        return None


def load_crime_scene_report_data():
    data = [
        {
            "date": "2002-12-01",
            "location": "SQL City",
            "officer": "Jimmy John",
            "description": "Well... you see... there wasn't a single lead",
        },
    ]
    return data


def save_crime_scene_report_data(data):
    for item in data:
        create_crime_scene_report(
            item["date"], item["location"], item["officer"], item["description"]
        )
