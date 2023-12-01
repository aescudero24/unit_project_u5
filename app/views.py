from django.shortcuts import render
from django.http.request import HttpRequest
from django.http.response import HttpResponse

from app import models
from app.forms import CrimeSceneReportForm

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
    return render(request, "home.html")


def drivers_view(request: HttpRequest) -> HttpResponse:
    return render(request, "home.html")


def library_view(request: HttpRequest) -> HttpResponse:
    return render(request, "home.html")


def interrogation_view(request: HttpRequest) -> HttpResponse:
    return render(request, "home.html")


def solve_view(request: HttpRequest) -> HttpResponse:
    return render(request, "home.html")
