from django.test import TestCase
from django.core.exceptions import ValidationError
from .models import ServiceCategory, Service

class ServiceCategoryModelTest(TestCase):
    
    def setUp(self):
        self.category = ServiceCategory.objects.create(
            name="Web Development",
            slug="web-development"
        )

    def test_service_category_creation(self):
        self.assertEqual(self.category.name, "Web Development")
        self.assertEqual(self.category.slug, "web-development")

    def test_service_category_string_representation(self):
        self.assertEqual(str(self.category), "Web Development")

    def test_service_category_ordering(self):
        category1 = ServiceCategory.objects.create(
            name="Graphic Design",
            slug="graphic-design"
        )
        category2 = ServiceCategory.objects.create(
            name="App Development",
            slug="app-development"
        )
        categories = list(ServiceCategory.objects.all())
        self.assertEqual(categories[0], category2)
        self.assertEqual(categories[1], category1)
        self.assertEqual(categories[2], self.category)


class ServiceModelTest(TestCase):
    
    def setUp(self):
        self.category = ServiceCategory.objects.create(
            name="Web Development",
            slug="web-development"
        )
        self.service = Service.objects.create(
            name="Website Creation",
            category=self.category,
            min_terms=5,
            price=1500.00,
            slug="website-creation"
        )

    def test_service_creation(self):
        self.assertEqual(self.service.name, "Website Creation")
        self.assertEqual(self.service.category, self.category)
        self.assertEqual(self.service.min_terms, 5)
        self.assertEqual(self.service.price, 1500.00)
        self.assertEqual(self.service.slug, "website-creation")

    def test_service_price_validation(self):
        service = Service(
            name="SEO Optimization",
            category=self.category,
            min_terms=2,
            price=-100.00,  # Invalid price, should raise ValidationError
            slug="seo-optimization"
        )
        with self.assertRaises(ValidationError):
            service.full_clean()

    def test_service_string_representation(self):
        self.assertEqual(str(self.service), "Web Development | Website Creation: min 5 днів, 1500.0₴")

    def test_service_ordering(self):
        service1 = Service.objects.create(
            name="SEO Optimization",
            category=self.category,
            min_terms=2,
            price=500.00,
            slug="seo-optimization"
        )
        service2 = Service.objects.create(
            name="E-commerce Site",
            category=self.category,
            min_terms=10,
            price=3000.00,
            slug="ecommerce-site"
        )
        services = list(Service.objects.all())
        self.assertEqual(services[0], service2)
        self.assertEqual(services[1], service1)
        self.assertEqual(services[2], self.service)
