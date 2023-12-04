from django.shortcuts import render
from django.http.request import HttpRequest
from django.http.response import HttpResponse

from app import models
from app.forms import (
    CrimeSceneReportForm,
    SuspectForm,
    DriversLicenseForm,
    LibraryCardForm,
    InterviewForm,
    SolveMysteryForm,
)

# Create your views here.


def home_view(request: HttpRequest) -> HttpResponse:
    return render(request, "home.html")


def crime_scene_report_view(request: HttpRequest) -> HttpResponse:
    if models.CrimeSceneReport.objects.all().count() == 0:
        crime_scene_report_data = models.load_crime_scene_report_data()
        models.save_crime_scene_report_data(crime_scene_report_data)
    form = CrimeSceneReportForm(request.GET)
    if form.is_valid():
        date = form.cleaned_data["date"]
        location = form.cleaned_data["location"]
        officer = form.cleaned_data["officer"]
        all_reports = models.all_crime_scene_reports()
        filtered_reports = models.find_crime_scene_reports(date, location, officer)
        return render(
            request,
            "report.html",
            {
                "form": form,
                "all_reports": all_reports,
                "filtered_reports": filtered_reports,
            },
        )
    return render(request, "report.html", {"form": form})


def suspects_view(request: HttpRequest) -> HttpResponse:
    if models.Suspect.objects.all().count() == 0:
        suspect_data = models.load_suspect_data()
        models.save_suspect_data(suspect_data)
    form = SuspectForm(request.GET)
    if form.is_valid():
        personal_id = form.cleaned_data["personal_id"]
        first_name = form.cleaned_data["first_name"]
        last_name = form.cleaned_data["last_name"]
        drivers_license_id = form.cleaned_data["drivers_license_id"]
        all_suspects = models.all_suspects()
        filtered_suspects = models.find_suspect(
            personal_id, first_name, last_name, drivers_license_id
        )
        return render(
            request,
            "suspects.html",
            {
                "form": form,
                "all_suspects": all_suspects,
                "filtered_suspects": filtered_suspects,
            },
        )
    return render(request, "suspects.html", {"form": form})


def drivers_view(request: HttpRequest) -> HttpResponse:
    if models.DriversLicense.objects.all().count() == 0:
        drivers_license_data = models.load_drivers_license_data()
        models.save_drivers_license_data(drivers_license_data)
    form = DriversLicenseForm(request.GET)
    if form.is_valid():
        license_id = form.cleaned_data["license_id"]
        age = form.cleaned_data["age"]
        height = form.cleaned_data["height"]
        hair_color = form.cleaned_data["hair_color"]
        gender = form.cleaned_data["gender"]
        all_licenses = models.all_licenses()
        filtered_licenses = models.find_license(
            license_id, age, height, hair_color, gender
        )
        return render(
            request,
            "drivers.html",
            {
                "form": form,
                "all_licenses": all_licenses,
                "filtered_licenses": filtered_licenses,
            },
        )
    return render(request, "drivers.html", {"form": form})


def library_view(request: HttpRequest) -> HttpResponse:
    if models.LibraryCard.objects.all().count() == 0:
        library_card_data = models.load_library_card_data()
        models.save_library_card_data(library_card_data)
    form = LibraryCardForm(request.GET)
    if form.is_valid():
        aisle = form.cleaned_data["aisle"]
        books = form.cleaned_data["books"]
        all_cards = models.all_library_cards()
        filtered_cards = models.find_library_card(aisle, books)
        return render(
            request,
            "library.html",
            {
                "form": form,
                "all_cards": all_cards,
                "filtered_cards": filtered_cards,
            },
        )
    return render(request, "library.html", {"form": form})


def interrogation_view(request: HttpRequest) -> HttpResponse:
    if models.Interview.objects.all().count() == 0:
        interview_data = models.load_interview_data()
        models.save_interview_data(interview_data)
    form = InterviewForm(request.GET)
    if form.is_valid():
        personal_id = form.cleaned_data["personal_id"]
        all_interviews = models.all_interviews()
        filtered_interviews = models.find_interview(personal_id)
        return render(
            request,
            "interrogation.html",
            {
                "form": form,
                "all_interviews": all_interviews,
                "filtered_interviews": filtered_interviews,
            },
        )
    return render(request, "interrogation.html", {"form": form})


def solve_view(request: HttpRequest) -> HttpResponse:
    result = ""
    form = SolveMysteryForm(request.GET)
    if form.is_valid():
        personal_id = form.cleaned_data["personal_id"]
        full_name = form.cleaned_data["full_name"]
        if personal_id == 1475 and full_name == "Jeremy Bowers":
            result = "This is him! We found our killer!"
        else:
            result = "Sorry, this is not our killer..."
    return render(request, "solve.html", {"form": form, "result": result})
