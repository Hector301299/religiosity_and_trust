from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Introduction(Page):
    pass


class Send(Page):
    """Only for Participant A"""
    form_model = 'group'
    form_fields = ['sent_amount']

    def is_displayed(self):
        return self.player.id_in_group == 1


class SendBackWaitPage(WaitPage):
    pass

class SendBack(Page):
    """Only for Participant B"""
    form_model = 'group'
    form_fields = ['sent_back_amount']

    def is_displayed(self):
        return self.player.id_in_group == 2
    
    def vars_for_template(self):
        tripled_amount = self.group.sent_amount * Constants.multiplier
        return dict(
            tripled_amount=tripled_amount,
        )        

class ResultsWaitPage(WaitPage):
    after_all_players_arrive = 'set_payoffs'

class Results(Page):
    """Earnings of each Participant"""
    def vars_for_template(self):
        return dict(tripled_amount=self.group.sent_amount * Constants.multiplier)


page_sequence = [
    Introduction,
    Send,
    SendBackWaitPage,
    SendBack,
    ResultsWaitPage,
    Results,
]
