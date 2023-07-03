from django.test import TestCase

from pulse_survey.survey import models


class FeedbackModelTest(TestCase):
    def test_feedback_saved(self):
        feedback = models.Feedback(email="Test@Example.Com", content="Some feedback")
        feedback.save()
        self.assertEqual(feedback.content, "Some feedback")

    def test_feedback_lower(self):
        feedback = models.Feedback(email="Test2@Example.Com", content="Some feedback")
        feedback.save()
        self.assertTrue(feedback.email.islower)