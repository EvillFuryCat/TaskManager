import factory


from task_manager.main.models import User, Tag, Task
from Faker import faker


class UserFactory(factory.django.DjangoModelFactory):
    username = factory.LazyAttribute(lambda _: faker.user_name())
    first_name = factory.LazyAttribute(lambda _: faker.first_name())
    last_name = factory.LazyAttribute(lambda _: faker.last_name())
    email = factory.LazyAttribute(lambda _: faker.unique.email())
    date_of_birth = factory.LazyAttribute(lambda _: faker.date())
    phone = factory.LazyAttribute(lambda _: faker.unique.phone_number())

    class Meta:
        model = User


class TagFactory(factory.django.DjangoModelFactory):
    title = factory.LazyAttribute(lambda _: faker.unique.word())

    class Meta:
        model = Tag
