from django.test import TestCase
from cars.models import Car


class CarModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Car.objects.create(name='FXX K', mark='Ferrari')

    def test_name(self):
        car = Car.objects.get(id=1)
        field_label = car._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'name')
        print(car)

    def test_name_max_length(self):
        car = Car.objects.get(id=1)
        max_length = car._meta.get_field('name').max_length
        self.assertEquals(max_length, 128)
        print(car)


class TestRandom(TestCase):
    def setUp(self):
        self.car = 1

    def tearDown(self):
        del self.car

    def test_1(self):
        self.assertNotEqual(self.car, 2)

    def test_2(self):
        assert self.car != 2

    def test_fail(self):
        assert self.car == 2



