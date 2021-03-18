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
import random


author = 'Hector Camacho'

doc = """
Un cuestionario simple sobre diversos temas de opinión. Parte del experimento de Religiosidad y Confianza basado en:
Tan, J. H., & Vogel, C. (2008). Religion and trust: An experimental study. Journal of Economic Psychology, 29(6), 832-848.
"""


class Constants(BaseConstants):
    name_in_url = 'survey'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):

    #-------------- Preguntas demográficas ------------------#

    gender = models.StringField(
        label="¿Cuál es su género?",
        choices=["Hombre","Mujer"],
        widget=widgets.RadioSelect
    )
    age = models.IntegerField(label="Ingrese su edad (en años cumplidos).", min=14, max=90)
    educ = models.StringField(
        label="¿Cuál es el último año o grado de estudios que aprobó?",
        choices=[
            "Sin nivel",
            "Primaria completa",
            "Secundaria Completa",
            "Superior no Universitaria",
            "Superior Universitaria",
            "Maestria/Doctorado"
        ],
        widget=widgets.RadioSelect
    )

    #------------------ Cuestionario ------------------------#

    q1 = models.StringField(
        label="¿Qué opinas de la inmortalidad?",
        widget=widgets.RadioSelect
    )
    def q1_choices(player):
        choices=[
            "No creo en la inmortalidad de ninguna manera.",
            "Creo en el renacimiento.",
            "Creo que la inmortalidad es la influencia continua de la vida de una persona en la familia o la sociedad.",
            "Incluso si el significado es un poco vago, creo en la existencia continuada de la personalidad como parte del principio espiritual que lo abarca todo.",
            "Creo en la resurrección y el más allá."
        ]
        random.shuffle(choices)
        return choices

    q2 = models.StringField(
        label="¿Qué crees que pasará después de la muerte?",
        widget=widgets.RadioSelect
    )
    def q2_choices(player):
        choices=[
            "Simplemente dejo de existir.",
            "Renacimiento.",
            "No lo sé.",
            "No estoy seguro.",
            "Mi 'espíritu' experimentará alguna continuación en el universo.",
            "Dependiendo de la voluntad de Dios, iré al cielo o al infierno."
        ]
        random.shuffle(choices)
        return choices

    q3 = models.StringField(
        label="¿Qué crees acerca de Dios?",
        widget=widgets.RadioSelect
    )
    def q3_choices(player):
        choices=[
            "No creo en dios",
            "No sé si Dios existe, y probablemente no haya forma de averiguarlo.",
            "Dios es un 'espíritu' en nosotros.",
            "No creo en ningún Dios personal, pero creo en algún ser superior.",
            "Siento que creo en Dios aunque no puedo explicar quién o qué es exactamente Dios.",
            "Sé que Dios realmente existe y no tengo ninguna duda al respecto."
        ]
        random.shuffle(choices)
        return choices
#    ed = models.BooleanField(
#        label="Are you left
# -handed?",
#        choices=[
#            [True,"Yes"],[False,"No"],
#        ]
#    )

