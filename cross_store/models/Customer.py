from django.db import models


class Customer(models.Model):
    email = models.EmailField()
    password = models.CharField(max_length=100)
    country = models.CharField(max_length=50, blank=True)
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    locality = models.CharField(max_length=100, blank=True)
    street_and_house = models.CharField(max_length=200, blank=True)
    index = models.CharField(max_length=50, blank=True)
    phone = models.CharField(max_length=10, blank=True)

    def create_customer(self, email: str, password: str, country: str,
                        first_name: str, last_name: str, locality: str, street_and_house: str, index: str, phone: str):
        self.email = email
        self.password = password
        self.country = country
        self.first_name = first_name
        self.last_name = last_name
        self.locality = locality
        self.street_and_house = street_and_house
        self.index = index
        self.phone = phone
        self.save()

    @staticmethod
    def get_customer_by_email(email: str):
        try:
            return Customer.objects.get(email=email)
        except:
            return False

    def is_exists(self):
        if Customer.objects.filter(email=self.email):
            return True

        return False
