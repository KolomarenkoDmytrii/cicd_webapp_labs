from django.test import TestCase
from django.core.exceptions import ValidationError
from .models import Feedback, ContactInfo

class FeedbackModelTest(TestCase):

    def setUp(self):
        self.feedback = Feedback.objects.create(
            user_name="John Doe",
            text="This is a great service!",
            rating=4
        )

    def test_feedback_creation(self):
        self.assertEqual(self.feedback.user_name, "John Doe")
        self.assertEqual(self.feedback.text, "This is a great service!")
        self.assertEqual(self.feedback.rating, 4)
        self.assertIsNotNone(self.feedback.published_at)

    def test_feedback_rating_validation(self):
        feedback = Feedback(
            user_name="Jane Doe",
            text="Not bad",
            rating=6  # Invalid rating, should raise ValidationError
        )
        with self.assertRaises(ValidationError):
            feedback.full_clean()

    def test_feedback_string_representation(self):
        self.assertEqual(str(self.feedback), "This is a great service!... - John Doe, 4")

    def test_feedback_ordering(self):
        feedback_earlier = Feedback.objects.create(
            user_name="Jane Doe",
            text="Earlier feedback",
            rating=4
        )
        feedback_later = Feedback.objects.create(
            user_name="John Smith",
            text="Later feedback",
            rating=5
        )
        feedbacks = list(Feedback.objects.all())
        self.assertEqual(feedbacks[0], feedback_later)
        self.assertEqual(feedbacks[1], feedback_earlier)


class ContactInfoModelTest(TestCase):

    def setUp(self):
        self.contact_info = ContactInfo.objects.create(
            user_name="Alice",
            email="alice@example.com",
            message="I need more information."
        )

    def test_contact_info_creation(self):
        self.assertEqual(self.contact_info.user_name, "Alice")
        self.assertEqual(self.contact_info.email, "alice@example.com")
        self.assertEqual(self.contact_info.message, "I need more information.")
        self.assertIsNotNone(self.contact_info.published_at)

    def test_contact_info_string_representation(self):
        self.assertEqual(str(self.contact_info), "I need more information.... - Alice, alice@example.com")

    def test_contact_info_ordering(self):
        contact_info_earlier = ContactInfo.objects.create(
            user_name="Bob",
            email="bob@example.com",
            message="Earlier message."
        )
        contact_info_later = ContactInfo.objects.create(
            user_name="Charlie",
            email="charlie@example.com",
            message="Later message."
        )
        contact_infos = list(ContactInfo.objects.all())
        self.assertEqual(contact_infos[0], contact_info_later)
        self.assertEqual(contact_infos[1], contact_info_earlier)
