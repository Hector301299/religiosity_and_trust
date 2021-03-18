from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
import random
import json

class Introduccion(Page):
    def is_displayed(self):
        return self.round_number == 1

class Demographics(Page):
    form_model = "player"
    form_fields = ["gender","age","educ"]

class SurveyQuestions(Page):
    form_model = "player"
    fields = [
        "q1",
        "q2",
        "q3"
    ]

    #def get_form_fields(self):
    #    fields = self.form_fields
    #    random.shuffle(fields)
    #    return fields
    def get_form_fields(self):
        form_field = self.fields
        random.shuffle(form_field)
        return form_field

page_sequence = [Introduccion,Demographics,SurveyQuestions,]