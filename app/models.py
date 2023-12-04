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
            "date": "2023-01-08",
            "location": "SQL City",
            "officer": "Johnson",
            "description": "Burglary - forced entry, stolen electronics",
        },
        {
            "date": "2023-02-17",
            "location": "Terminal City",
            "officer": "Miller",
            "description": "Assault - bar fight, minor injuries reported",
        },
        {
            "date": "2023-03-25",
            "location": "Django City",
            "officer": "Brown",
            "description": "Robbery - armed robbery at convenience store",
        },
        {
            "date": "2023-04-12",
            "location": "SQL City",
            "officer": "Davis",
            "description": "Theft - shoplifting incident at a mall",
        },
        {
            "date": "2023-05-19",
            "location": "SQL City",
            "officer": "Taylor",
            "description": "Vandalism - graffiti on public property",
        },
        {
            "date": "2023-06-04",
            "location": "Terminal City",
            "officer": "Clark",
            "description": "Domestic Dispute - argument between family members",
        },
        {
            "date": "2023-07-22",
            "location": "Terminal City",
            "officer": "White",
            "description": "Traffic Accident - collision with property damage",
        },
        {
            "date": "2023-08-09",
            "location": "Django City",
            "officer": "Smith",
            "description": "Arson - fire set intentionally, no injuries reported",
        },
        {
            "date": "2023-09-30",
            "location": "Django City",
            "officer": "Johnson",
            "description": "Fraud - online scam, financial loss reported",
        },
        {
            "date": "2023-10-15",
            "location": "Django City",
            "officer": "Davenport",
            "description": "Missing Person - person reported missing, investigation ongoing",
        },
        {
            "date": "2023-11-07",
            "location": "SQL City",
            "officer": "Brown",
            "description": "Drug Possession - arrest made for illegal substance",
        },
        {
            "date": "2023-12-28",
            "location": "Terminal City",
            "officer": "Davis",
            "description": "Fraud - credit card fraud, investigation in progress",
        },
        {
            "date": "2023-05-30",
            "location": "Base Camp Coding Academy",
            "officer": "Cohen",
            "description": "Disturbance - new students",
        },
        {
            "date": "2023-11-30",
            "location": "Base Camp Coding Academy",
            "officer": "Cohen",
            "description": "Professional Write-up - ping-pong during solo time",
        },
        {
            "date": "2023-03-19",
            "location": "Django City",
            "officer": "Davenport",
            "description": "Robbery - theft of personal belongings at knifepoint",
        },
        {
            "date": "2023-04-05",
            "location": "Terminal City",
            "officer": "Smith",
            "description": "Theft - stolen bicycle from a residential area",
        },
        {
            "date": "2023-05-27",
            "location": "Terminal City",
            "officer": "Johnson",
            "description": "Vandalism - damaged car windows, motive unknown",
        },
        {
            "date": "2023-06-14",
            "location": "SQL City",
            "officer": "Miller",
            "description": "Domestic Dispute - disagreement between spouses, no violence",
        },
        {
            "date": "2023-07-03",
            "location": "SQL City",
            "officer": "Brown",
            "description": "Traffic Accident - rear-end collision, no injuries reported",
        },
        {
            "date": "2023-08-20",
            "location": "Django City",
            "officer": "Davis",
            "description": "Arson - fire set at abandoned building, no injuries reported",
        },
        {
            "date": "2023-09-12",
            "location": "Terminal City",
            "officer": "Taylor",
            "description": "Fraud - identity theft, victim seeking restitution",
        },
        {
            "date": "2023-10-01",
            "location": "SQL City",
            "officer": "Clark",
            "description": "Missing Person - located safe and sound, case closed",
        },
        {
            "date": "2023-11-25",
            "location": "Terminal City",
            "officer": "Davenport",
            "description": "Drug Possession - arrest made for illegal substance",
        },
        {
            "date": "2023-12-02",
            "location": "SQL City",
            "officer": "Smith",
            "description": "Fraud - email phishing scam, financial loss reported",
        },
        {
            "date": "2023-11-30",
            "location": "Django City",
            "officer": "Davenport",
            "description": "Homicide - victim's last name is Martinez - witnesses include brother Ruben and friend Preston Lee",
        },
        {
            "date": "2023-02-10",
            "location": "SQL City",
            "officer": "Miller",
            "description": "Assault - physical altercation at a bar, one person arrested",
        },
        {
            "date": "2023-03-30",
            "location": "Terminal City",
            "officer": "Brown",
            "description": "Robbery - armed robbery at a gas station",
        },
        {
            "date": "2023-04-19",
            "location": "Django City",
            "officer": "Davis",
            "description": "Theft - stolen package from a front porch",
        },
        {
            "date": "2023-05-08",
            "location": "Terminal City",
            "officer": "Taylor",
            "description": "Vandalism - graffiti on public art installation",
        },
        {
            "date": "2023-06-27",
            "location": "SQL City",
            "officer": "Clark",
            "description": "Domestic Dispute - family argument, no legal action taken",
        },
        {
            "date": "2023-07-15",
            "location": "SQL City",
            "officer": "White",
            "description": "Traffic Accident - hit-and-run incident, investigation ongoing",
        },
        {
            "date": "2023-08-06",
            "location": "Terminal City",
            "officer": "Smith",
            "description": "Arson - fire set in a dumpster, no injuries reported",
        },
        {
            "date": "2023-09-23",
            "location": "Django City",
            "officer": "Johnson",
            "description": "Fraud - counterfeit currency, suspect at large",
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
            "personal_id": 4219,
            "first_name": "Brian",
            "last_name": "Mullen",
            "drivers_license_id": 6423,
        },
        {
            "personal_id": 6542,
            "first_name": "Amanda",
            "last_name": "Baker",
            "drivers_license_id": 8217,
        },
        {
            "personal_id": 2873,
            "first_name": "Daniel",
            "last_name": "Reyes",
            "drivers_license_id": 1548,
        },
        {
            "personal_id": 9136,
            "first_name": "Melissa",
            "last_name": "Gomez",
            "drivers_license_id": 7364,
        },
        {
            "personal_id": 5729,
            "first_name": "Jeremy",
            "last_name": "Carter",
            "drivers_license_id": 3956,
        },
        {
            "personal_id": 6498,
            "first_name": "Ruben",
            "last_name": "Martinez",
            "drivers_license_id": 2871,
        },
        {
            "personal_id": 1247,
            "first_name": "Victor",
            "last_name": "Howard",
            "drivers_license_id": 4692,
        },
        {
            "personal_id": 8564,
            "first_name": "Katherine",
            "last_name": "Morgan",
            "drivers_license_id": 5738,
        },
        {
            "personal_id": 3982,
            "first_name": "Joe",
            "last_name": "Germuska",
            "drivers_license_id": 8741,
        },
        {
            "personal_id": 7361,
            "first_name": "Megan",
            "last_name": "Cooper",
            "drivers_license_id": 2987,
        },
        {
            "personal_id": 5814,
            "first_name": "Keith",
            "last_name": "Richardson",
            "drivers_license_id": 7425,
        },
        {
            "personal_id": 9263,
            "first_name": "Tiffany",
            "last_name": "Perez",
            "drivers_license_id": 6149,
        },
        {
            "personal_id": 1475,
            "first_name": "Jeremy",
            "last_name": "Bowers",
            "drivers_license_id": 5566,
        },
        {
            "personal_id": 6329,
            "first_name": "Jennifer",
            "last_name": "Mitchell",
            "drivers_license_id": 2957,
        },
        {
            "personal_id": 5712,
            "first_name": "Aaron",
            "last_name": "Russell",
            "drivers_license_id": 4871,
        },
        {
            "personal_id": 4836,
            "first_name": "Cassandra",
            "last_name": "Fisher",
            "drivers_license_id": 6714,
        },
        {
            "personal_id": 3591,
            "first_name": "Evan",
            "last_name": "Simmons",
            "drivers_license_id": 8236,
        },
        {
            "personal_id": 7952,
            "first_name": "Lindsay",
            "last_name": "Watson",
            "drivers_license_id": 4183,
        },
        {
            "personal_id": 6427,
            "first_name": "Benjamin",
            "last_name": "Turner",
            "drivers_license_id": 5391,
        },
        {
            "personal_id": 8741,
            "first_name": "Preston",
            "last_name": "Lee",
            "drivers_license_id": 6732,
        },
        {
            "personal_id": 2916,
            "first_name": "Derek",
            "last_name": "Gardner",
            "drivers_license_id": 1984,
        },
        {
            "personal_id": 5482,
            "first_name": "Lauren",
            "last_name": "Fletcher",
            "drivers_license_id": 7246,
        },
        {
            "personal_id": 7135,
            "first_name": "Timothy",
            "last_name": "Peters",
            "drivers_license_id": 3657,
        },
        {
            "personal_id": 1674,
            "first_name": "Sara",
            "last_name": "Fleming",
            "drivers_license_id": 9281,
        },
        {
            "personal_id": 8246,
            "first_name": "Philip",
            "last_name": "Andrews",
            "drivers_license_id": 5723,
        },
        {
            "personal_id": 4251,
            "first_name": "Rachel",
            "last_name": "Barnes",
            "drivers_license_id": 8712,
        },
        {
            "personal_id": 6983,
            "first_name": "Austin",
            "last_name": "Ward",
            "drivers_license_id": 6398,
        },
        {
            "personal_id": 1528,
            "first_name": "Haley",
            "last_name": "Wallace",
            "drivers_license_id": 7852,
        },
        {
            "personal_id": 4673,
            "first_name": "Oscar",
            "last_name": "Reed",
            "drivers_license_id": 9514,
        },
        {
            "personal_id": 5982,
            "first_name": "Jasmine",
            "last_name": "Sullivan",
            "drivers_license_id": 6147,
        },
        {
            "personal_id": 3276,
            "first_name": "Nathan",
            "last_name": "Hayes",
            "drivers_license_id": 8734,
        },
        {
            "personal_id": 8459,
            "first_name": "Holly",
            "last_name": "Wagner",
            "drivers_license_id": 5182,
        },
        {
            "personal_id": 5134,
            "first_name": "Logan",
            "last_name": "Murray",
            "drivers_license_id": 7823,
        },
    ]
    return data


def save_suspect_data(data):
    for item in data:
        create_suspect(
            item["personal_id"],
            item["first_name"],
            item["last_name"],
            item["drivers_license_id"],
        )


### LICENSE ###
class DriversLicense(models.Model):
    license_id = models.IntegerField()
    age = models.IntegerField()
    height = models.IntegerField()
    hair_color = models.TextField()
    gender = models.TextField()


def create_license(
    license_id,
    age,
    height,
    hair_color,
    gender,
):
    license = DriversLicense(
        license_id=license_id,
        age=age,
        height=height,
        hair_color=hair_color,
        gender=gender,
    )
    license.save()
    return license


def all_licenses():
    return DriversLicense.objects.all()


def find_license(license_id, age, height, hair_color, gender):
    licenses = all_licenses()
    if license_id:
        licenses = licenses.filter(license_id=license_id)
    if age:
        licenses = licenses.filter(age=age)
    if age:
        licenses = licenses.filter(height=height)
    if height:
        licenses = licenses.filter(hair_color=hair_color)
    if gender:
        licenses = licenses.filter(gender=gender)
    return licenses


def load_drivers_license_data():
    data = [
        {
            "license_id": 8217,
            "age": 35,
            "height": 169,
            "hair_color": "Brunette",
            "gender": "Female",
        },
        {
            "license_id": 5566,
            "age": 42,
            "height": 181,
            "hair_color": "Black",
            "gender": "Male",
        },
        {
            "license_id": 1234,
            "age": 28,
            "height": 175,
            "hair_color": "Brown",
            "gender": "Male",
        },
        {
            "license_id": 5678,
            "age": 35,
            "height": 162,
            "hair_color": "Blonde",
            "gender": "Female",
        },
        {
            "license_id": 9101,
            "age": 42,
            "height": 180,
            "hair_color": "Black",
            "gender": "Male",
        },
        {
            "license_id": 2345,
            "age": 29,
            "height": 168,
            "hair_color": "Red",
            "gender": "Female",
        },
        {
            "license_id": 6789,
            "age": 56,
            "height": 175,
            "hair_color": "Brown",
            "gender": "Male",
        },
        {
            "license_id": 8741,
            "age": 24,
            "height": 180,
            "hair_color": "Blonde",
            "gender": "Male",
        },
        {
            "license_id": 3344,
            "age": 38,
            "height": 185,
            "hair_color": "Black",
            "gender": "Male",
        },
        {
            "license_id": 5566,
            "age": 31,
            "height": 175,
            "hair_color": "Brown",
            "gender": "Female",
        },
        {
            "license_id": 7788,
            "age": 49,
            "height": 170,
            "hair_color": "Red",
            "gender": "Male",
        },
        {
            "license_id": 9900,
            "age": 27,
            "height": 163,
            "hair_color": "Blonde",
            "gender": "Female",
        },
        {
            "license_id": 1122,
            "age": 40,
            "height": 178,
            "hair_color": "Black",
            "gender": "Male",
        },
        {
            "license_id": 3344,
            "age": 33,
            "height": 172,
            "hair_color": "Brown",
            "gender": "Female",
        },
        {
            "license_id": 5566,
            "age": 45,
            "height": 175,
            "hair_color": "Red",
            "gender": "Male",
        },
        {
            "license_id": 7788,
            "age": 29,
            "height": 160,
            "hair_color": "Blonde",
            "gender": "Female",
        },
        {
            "license_id": 8741,
            "age": 52,
            "height": 183,
            "hair_color": "Black",
            "gender": "Male",
        },
        {
            "license_id": 1122,
            "age": 36,
            "height": 167,
            "hair_color": "Brown",
            "gender": "Female",
        },
        {
            "license_id": 3344,
            "age": 44,
            "height": 175,
            "hair_color": "Red",
            "gender": "Male",
        },
        {
            "license_id": 5566,
            "age": 30,
            "height": 162,
            "hair_color": "Blonde",
            "gender": "Female",
        },
        {
            "license_id": 7788,
            "age": 48,
            "height": 180,
            "hair_color": "Black",
            "gender": "Male",
        },
        {
            "license_id": 9900,
            "age": 25,
            "height": 165,
            "hair_color": "Brown",
            "gender": "Female",
        },
        {
            "license_id": 1122,
            "age": 39,
            "height": 176,
            "hair_color": "Red",
            "gender": "Male",
        },
        {
            "license_id": 3344,
            "age": 32,
            "height": 168,
            "hair_color": "Blonde",
            "gender": "Female",
        },
        {
            "license_id": 5566,
            "age": 46,
            "height": 174,
            "hair_color": "Black",
            "gender": "Male",
        },
        {
            "license_id": 7788,
            "age": 28,
            "height": 163,
            "hair_color": "Brown",
            "gender": "Female",
        },
        {
            "license_id": 9900,
            "age": 53,
            "height": 182,
            "hair_color": "Red",
            "gender": "Male",
        },
        {
            "license_id": 1122,
            "age": 37,
            "height": 166,
            "hair_color": "Blonde",
            "gender": "Female",
        },
        {
            "license_id": 3344,
            "age": 43,
            "height": 175,
            "hair_color": "Black",
            "gender": "Male",
        },
        {
            "license_id": 5566,
            "age": 31,
            "height": 160,
            "hair_color": "Brown",
            "gender": "Female",
        },
        {
            "license_id": 7788,
            "age": 50,
            "height": 178,
            "hair_color": "Red",
            "gender": "Male",
        },
        {
            "license_id": 9900,
            "age": 26,
            "height": 164,
            "hair_color": "Blonde",
            "gender": "Female",
        },
        {
            "license_id": 1122,
            "age": 41,
            "height": 177,
            "hair_color": "Black",
            "gender": "Male",
        },
    ]
    return data


def save_drivers_license_data(data):
    for item in data:
        create_license(
            item["license_id"],
            item["age"],
            item["height"],
            item["hair_color"],
            item["gender"],
        )


### LIBRARY ###
class LibraryCard(models.Model):
    last_name = models.TextField()
    aisle = models.IntegerField()
    books = models.IntegerField()


def create_library_card(
    last_name,
    aisle,
    books,
):
    card = LibraryCard(
        last_name=last_name,
        aisle=aisle,
        books=books,
    )
    card.save()
    return card


def all_library_cards():
    return LibraryCard.objects.all()


def find_library_card(aisle, books):
    cards = all_library_cards()
    if aisle:
        cards = cards.filter(aisle=aisle)
    if books:
        cards = cards.filter(books=books)
    return cards


def load_library_card_data():
    data = [
        {"last_name": "Smith", "aisle": 2, "books": 15},
        {"last_name": "Johnson", "aisle": 3, "books": 22},
        {"last_name": "Williams", "aisle": 1, "books": 10},
        {"last_name": "Jones", "aisle": 5, "books": 18},
        {"last_name": "Brown", "aisle": 4, "books": 12},
        {"last_name": "Davis", "aisle": 2, "books": 14},
        {"last_name": "Miller", "aisle": 3, "books": 20},
        {"last_name": "Wilson", "aisle": 1, "books": 8},
        {"last_name": "Moore", "aisle": 5, "books": 16},
        {"last_name": "Taylor", "aisle": 4, "books": 11},
        {"last_name": "Anderson", "aisle": 2, "books": 17},
        {"last_name": "Thomas", "aisle": 3, "books": 23},
        {"last_name": "Martinez", "aisle": 13, "books": 1},
        {"last_name": "White", "aisle": 5, "books": 13},
        {"last_name": "Harris", "aisle": 4, "books": 19},
        {"last_name": "Bowers", "aisle": 13, "books": 2},
        {"last_name": "Thompson", "aisle": 3, "books": 7},
        {"last_name": "Garcia", "aisle": 1, "books": 14},
        {"last_name": "Martinez", "aisle": 5, "books": 18},
        {"last_name": "Robinson", "aisle": 4, "books": 12},
        {"last_name": "Clark", "aisle": 2, "books": 16},
        {"last_name": "Rodriguez", "aisle": 3, "books": 9},
        {"last_name": "Lewis", "aisle": 1, "books": 22},
        {"last_name": "Lee", "aisle": 5, "books": 11},
        {"last_name": "Walker", "aisle": 4, "books": 20},
        {"last_name": "Lee", "aisle": 13, "books": 3},
        {"last_name": "Allen", "aisle": 3, "books": 13},
        {"last_name": "Young", "aisle": 1, "books": 7},
        {"last_name": "Hill", "aisle": 5, "books": 19},
        {"last_name": "Wright", "aisle": 4, "books": 10},
        {"last_name": "Lopez", "aisle": 2, "books": 17},
        {"last_name": "Green", "aisle": 3, "books": 23},
        {"last_name": "Adams", "aisle": 1, "books": 8},
    ]
    return data


def save_library_card_data(data):
    for item in data:
        create_library_card(
            item["last_name"],
            item["aisle"],
            item["books"],
        )


### INTERVIEW ###
class Interview(models.Model):
    personal_id = models.IntegerField()
    description = models.TextField()


def create_interview(personal_id, description):
    interview = Interview(
        personal_id=personal_id,
        description=description,
    )
    interview.save()
    return interview


def all_interviews():
    return Interview.objects.all()


def find_interview(personal_id):
    interviews = all_interviews()
    if personal_id:
        interviews = interviews.filter(personal_id=personal_id)
    return interviews


def load_interview_data():
    data = [
        {
            "personal_id": 1001,
            "description": "I saw a person wearing a red jacket near the crime scene.",
        },
        {
            "personal_id": 1002,
            "description": "I heard a loud noise around the time of the incident, but I didn't see anything.",
        },
        {
            "personal_id": 1003,
            "description": "I noticed a suspicious-looking individual acting nervously near the library entrance.",
        },
        {
            "personal_id": 1004,
            "description": "I saw someone running away from the crime scene, but I couldn't identify their face.",
        },
        {
            "personal_id": 1005,
            "description": "I observed a person wearing a mask entering the library just before the incident occurred.",
        },
        {
            "personal_id": 1006,
            "description": "I overheard a conversation mentioning something about a false fire alarm and property damage.",
        },
        {
            "personal_id": 1007,
            "description": "I didn't witness the crime directly, but I saw a group of people acting suspiciously in the library courtyard.",
        },
        {
            "personal_id": 1008,
            "description": "I saw someone with a backpack leaving the library in a hurry shortly after the incident.",
        },
        {
            "personal_id": 1009,
            "description": "I noticed a person with a distinctive tattoo near the crime scene.",
        },
        {
            "personal_id": 1010,
            "description": "I observed a person wearing gloves, which seemed unusual for the weather, near the library entrance.",
        },
        {
            "personal_id": 1011,
            "description": "I heard someone arguing loudly in the library, but I couldn't see who it was.",
        },
        {
            "personal_id": 1012,
            "description": "I noticed a person carrying a large bag entering the library, and they seemed nervous.",
        },
        {
            "personal_id": 1013,
            "description": "I witnessed a person filming something on their phone near the crime scene.",
        },
        {
            "personal_id": 1014,
            "description": "I saw someone wearing a hat and sunglasses trying to avoid being noticed in the library.",
        },
        {
            "personal_id": 1015,
            "description": "I observed a person leaving the library with a torn piece of paper, and they seemed in a hurry.",
        },
        {
            "personal_id": 1016,
            "description": "I noticed a person with a distinctive accent speaking loudly in the library just before the incident.",
        },
        {
            "personal_id": 1017,
            "description": "I saw someone with a backpack acting nervously near the fire alarm panel.",
        },
        {
            "personal_id": 1018,
            "description": "I overheard a conversation about a false fire alarm, and someone mentioned a damaged bookshelf.",
        },
        {
            "personal_id": 1019,
            "description": "I witnessed a person entering the library with a bag full of snacks, which seemed unusual for the situation.",
        },
        {
            "personal_id": 1020,
            "description": "I saw a person looking around suspiciously near the library computers.",
        },
        {
            "personal_id": 1021,
            "description": "I observed a person holding a suspicious-looking package entering the library just before the incident.",
        },
        {
            "personal_id": 1022,
            "description": "I heard someone talking about the false fire alarm and property damage in the library lobby.",
        },
        {
            "personal_id": 1023,
            "description": "I noticed a person with a backpack leaving the library in a hurry shortly after the incident.",
        },
        {
            "personal_id": 1024,
            "description": "I saw someone wearing gloves and carrying a toolbox near the library entrance.",
        },
        {
            "personal_id": 1025,
            "description": "I observed a person acting strangely and avoiding eye contact near the crime scene.",
        },
        {
            "personal_id": 1026,
            "description": "I overheard a conversation mentioning a false fire alarm and the sound of breaking glass in the library.",
        },
        {
            "personal_id": 1027,
            "description": "I witnessed a person with a backpack leaving the library quickly, and they looked nervous.",
        },
        {
            "personal_id": 1028,
            "description": "I saw someone with a suspicious-looking bag entering the library just before the incident.",
        },
        {
            "personal_id": 1029,
            "description": "I noticed a person with a distinct hairstyle near the crime scene.",
        },
        {
            "personal_id": 1030,
            "description": "I observed a person wearing a hoodie and sunglasses entering the library, and they seemed out of place.",
        },
        {
            "personal_id": 1031,
            "description": "I heard a loud noise in the library and saw someone leaving in a hurry, but I couldn't identify them.",
        },
        {
            "personal_id": 1032,
            "description": "I noticed a person carrying a backpack and acting suspiciously near the fire exit.",
        },
        {
            "personal_id": 1033,
            "description": "I saw someone wearing a mask and gloves near the library entrance, and they seemed in a rush.",
        },
    ]
    return data


def save_interview_data(data):
    for item in data:
        create_interview(
            item["personal_id"],
            item["description"],
        )
