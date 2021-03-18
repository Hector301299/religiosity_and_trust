from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c,
    currency_range,
)


author = 'Hector Camacho'

doc = """
Este es un Trust Game (Experimento de Confianza) en donde el monto propuesto por el primer jugador 
se triplica y el segundo jugador debe decidir el monto a devolver al primer jugador, a ciegas. Este juego 
está basado en Berg, Dickhaut and McCabe (1995).
"""


class Constants(BaseConstants):
    name_in_url = 'trust_game'
    players_per_group = 2
    num_rounds = 10

    instructions_template = 'trust_game/Instructions.html'
    
    endowment = c(10)
    multiplier = 3

class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    sent_amount = models.CurrencyField(
        min=0,
        max=Constants.endowment,
        doc="""Cantidad enviada por el Participante A""",
        label="Por favor, ingrese una cantidad del 0 al 10:",
    )

    sent_back_amount = models.CurrencyField(
        doc="""Cantidad enviada por el Participante B""",
        label="Por favor, ingrese la cantidad que pasará al Participante A.",
        min=c(0),
    )
    
    #@property
    #def sent_back_amount(self):
    #    if self.sent_back_amount > self.sent_amount * Constants.multiplier:
    #        sent_back_amount = models.CurrencyField(c(self.sent_amount * Constants.multiplier))
    #        return self.sent_back_amount
    #    else:
    #        sent_back_amount = models.CurrencyField(c(self.sent_back_amount))
    #        return self.sent_back_amount

    #def sent_back_amount_max(self):
    #    return self.sent_amount * Constants.multiplier

    def set_payoffs(self):
        p1 = self.get_player_by_id(1)
        p2 = self.get_player_by_id(2)
        p1.payoff = Constants.endowment - self.sent_amount + self.sent_back_amount
        p2.payoff = self.sent_amount * Constants.multiplier - self.sent_back_amount


class Player(BasePlayer):
    pass
