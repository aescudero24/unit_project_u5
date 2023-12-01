from django.db import models


# Create your models here.


### CRIME SCENE REPORT ###
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


def find_crime_scene_reports(date, location, officer):
    reports = all_crime_scene_reports()
    if date:
        reports = reports.filter(date=date)
    if location:
        reports = reports.filter(location=location)
    if officer:
        reports = reports.filter(officer=officer)
    return reports


def load_crime_scene_report_data():
    data = [
        {
            "date": "2002-12-01",
            "location": "SQL City",
            "officer": "Smith",
            "description": "Vandalism - graffiti on wall",
        },
        {
            "date": "2005-08-17",
            "location": "SQL City",
            "officer": "Smith",
            "description": "Donuts - officers were eating donuts",
        },
        {
            "date": "2021-05-02",
            "location": "Terminal City",
            "officer": "Johnson",
            "description": "Theft - items stolen from store",
        },
        {
            "date": "2023-05-30",
            "location": "Base Camp Coding Academy",
            "officer": "Cohen",
            "description": "Disturbance - new students",
        },
        {
            "date": "2007-01-04",
            "location": "Terminal City",
            "officer": "Lewis",
            "description": "Burglary - residential building",
        },
        {
            "date": "2005-05-05",
            "location": "Terminal City",
            "officer": "Jones",
            "description": "Criminal Mischief - damaged store property",
        },
        {
            "date": "2023-11-30",
            "location": "Django City",
            "officer": "Davenport",
            "description": "Homicide - victim's name is Yasmin Martinez - witnesses include her brother Ruben and friend Frank Boles",
        },
        {
            "date": "2011-02-16",
            "location": "Terminal City",
            "officer": "Washington",
            "description": "Vehicle Crash - involved parties unharmed",
        },
        {
            "date": "2019-7-21",
            "location": "Terminal City",
            "officer": "Miller",
            "description": "Trespassing - individuals removed from property",
        },
        {
            "date": "2023-11-23",
            "location": "Base Camp Coding Academy",
            "officer": "Cohen",
            "description": "Professional Write-Up - ping pong during solo time",
        },
        {
            "date": "2021-04-14",
            "location": "Django City",
            "officer": "Taylor",
            "description": "Drugs - drug paraphernalia found on individuals",
        },
        {
            "date": "2022-02-28",
            "location": "Django City",
            "officer": "Moore",
            "description": "Battery - assault causing injury",
        },
        {
            "date": "2023-06-13",
            "location": "Django City",
            "officer": "Jackson",
            "description": "Fraud - check or credit card fraud reported",
        },
        {
            "date": "2023-12-01",
            "location": "SQL City",
            "officer": "White",
            "description": "Fire - false fire alarm, property damage",
        },
    ]
    return data


def save_crime_scene_report_data(data):
    for item in data:
        create_crime_scene_report(
            item["date"], item["location"], item["officer"], item["description"]
        )


### SUSPECT ###
class Suspect(models.Model):
    personal_id = models.IntegerField()
    first_name = models.TextField()
    last_name = models.TextField()
    drivers_license_id = models.IntegerField()


def create_suspect(
    personal_id,
    first_name,
    last_name,
    drivers_license_id,
):
    suspect = Suspect(
        personal_id=personal_id,
        first_name=first_name,
        last_name=last_name,
        drivers_license_id=drivers_license_id,
    )
    suspect.save()
    return suspect


def all_suspects():
    return Suspect.objects.all()


def find_suspect(personal_id, first_name, last_name, drivers_license_id):
    suspects = all_suspects()
    if personal_id:
        suspects = suspects.filter(personal_id=personal_id)
    if first_name:
        suspects = suspects.filter(first_name=first_name)
    if last_name:
        suspects = suspects.filter(last_name=last_name)
    if drivers_license_id:
        suspects = suspects.filter(drivers_license_id=drivers_license_id)
    return suspects


def load_suspect_data():
    data = [
        {
            "date": "2002-12-01",
            "location": "SQL City",
            "officer": "Smith",
            "description": "Vandalism - graffiti on wall",
        },
        {
            "date": "2005-08-17",
            "location": "SQL City",
            "officer": "Smith",
            "description": "Donuts - officers were eating donuts",
        },
        {
            "date": "2021-05-02",
            "location": "Terminal City",
            "officer": "Johnson",
            "description": "Theft - items stolen from store",
        },
        {
            "date": "2023-05-30",
            "location": "Base Camp Coding Academy",
            "officer": "Cohen",
            "description": "Disturbance - new students",
        },
        {
            "date": "2007-01-04",
            "location": "Terminal City",
            "officer": "Lewis",
            "description": "Burglary - residential building",
        },
        {
            "date": "2005-05-05",
            "location": "Terminal City",
            "officer": "Jones",
            "description": "Criminal Mischief - damaged store property",
        },
        {
            "date": "2023-11-30",
            "location": "Django City",
            "officer": "Davenport",
            "description": "Homicide - victim's name is Yasmin Martinez - witnesses include her brother Ruben and friend Frank Boles",
        },
        {
            "date": "2011-02-16",
            "location": "Terminal City",
            "officer": "Washington",
            "description": "Vehicle Crash - involved parties unharmed",
        },
        {
            "date": "2019-7-21",
            "location": "Terminal City",
            "officer": "Miller",
            "description": "Trespassing - individuals removed from property",
        },
        {
            "date": "2023-11-23",
            "location": "Base Camp Coding Academy",
            "officer": "Cohen",
            "description": "Professional Write-Up - ping pong during solo time",
        },
        {
            "date": "2021-04-14",
            "location": "Django City",
            "officer": "Taylor",
            "description": "Drugs - drug paraphernalia found on individuals",
        },
        {
            "date": "2022-02-28",
            "location": "Django City",
            "officer": "Moore",
            "description": "Battery - assault causing injury",
        },
        {
            "date": "2023-06-13",
            "location": "Django City",
            "officer": "Jackson",
            "description": "Fraud - check or credit card fraud reported",
        },
        {
            "date": "2023-12-01",
            "location": "SQL City",
            "officer": "White",
            "description": "Fire - false fire alarm, property damage",
        },
    ]
    return data


def save_crime_scene_report_data(data):
    for item in data:
        create_crime_scene_report(
            item["date"], item["location"], item["officer"], item["description"]
        )
