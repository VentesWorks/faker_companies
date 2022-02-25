import random

from faker import Faker

from rest_framework.views import APIView
from rest_framework.response import Response

random.seed(1000)

fake = Faker()
Faker.seed(4321)

INDUSTRIES = {
    1: "eCommerce",
    2: "Mining",
    3: "Technology",
    4: "Healthcare",
    5: "Military",
    6: "Aviation",
    7: "Agriculture",
    8: "Energy",
}

COUNTRY_CODES = [fake.country_code() for _ in range(10)]


COMPANIES = [
    {
        "_id": i,
        "company_industry": random.choice(list(INDUSTRIES.keys())),
        "company_location": random.choice(COUNTRY_CODES),
        "company_type": "public" if i < 51 else "private",
        "company_email": fake.email(),
        "company_name": fake.company(),
        "founded_on": fake.past_date(),
    }
    for i in range(1, 101)
]


class ListIndustries(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        return Response(INDUSTRIES)


class ListCompanies(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        return Response(COMPANIES)
