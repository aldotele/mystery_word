from django.test import TestCase, SimpleTestCase, override_settings
from django.urls import reverse
from mystery_app.models import Round


@override_settings(STATICFILES_STORAGE='django.contrib.staticfiles.storage.StaticFilesStorage')
class HomePageTests(SimpleTestCase):
    def test_home_page_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_by_name(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('index'))
        self.assertTemplateUsed(response, 'empty.html')
        self.assertTemplateUsed(response, 'index.html')


@override_settings(STATICFILES_STORAGE='django.contrib.staticfiles.storage.StaticFilesStorage')
class PlayPageTests(TestCase):
    hint_1 = "first hint"
    hint_2 = "second hint"
    hint_3 = "third hint"
    hint_4 = "fourth hint"
    hint_5 = "fifth hint"
    solution = "U09MVVRJT04="
    new_round = Round(hint_1=hint_1,
                      hint_2=hint_2,
                      hint_3=hint_3,
                      hint_4=hint_4,
                      hint_5=hint_5,
                      solution=solution)

    def test_play_page_status_code(self):
        self.new_round.save()
        response = self.client.get('/play/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_by_name(self):
        self.new_round.save()
        response = self.client.get(reverse('play'))
        self.assertEqual(response.status_code, 200)

    def test_rounds_on_db(self):
        self.new_round.save()
        self.assertEqual(Round.objects.all().count(), 1)
        self.assertEqual(Round.objects.all()[0].hint_1, self.hint_1)
        self.assertEqual(Round.objects.all()[0].hint_2, self.hint_2)
        self.assertEqual(Round.objects.all()[0].hint_3, self.hint_3)
        self.assertEqual(Round.objects.all()[0].hint_4, self.hint_4)
        self.assertEqual(Round.objects.all()[0].hint_5, self.hint_5)
        self.assertEqual(Round.objects.all()[0].solution, self.solution)