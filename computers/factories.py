import factory
import factory.fuzzy


class ComputerFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = "computers.Computer"
    name = factory.faker.Faker("name")
    description = factory.faker.Faker("name")
    mac_address = factory.faker.Faker("mac_address")
    ip_address = factory.faker.Faker("ip_address")
    employee_abbrev = factory.fuzzy.FuzzyText(length=3)
