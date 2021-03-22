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
    
      q4 = models.StringField(
        label="¿Qué piensas de Jesús?",
        widget=widgets.RadioSelect
    )
    def q4_choices(player):
        choices=[
            "Para ser honesto, no estoy seguro de si existió el Jesús histórico.",
            "Creo que Jesús era solo un ser humano.",
            "Creo que Jesús fue solo humano, pero extraordinario.",
            "Tengo la sensación de que Jesús fue un gran profeta religioso, pero ya no era el Hijo de Dios de lo que todos somos hijos de Dios.",
            "Jesús se entiende mejor como un símbolo de bondad, no importa si existió o no",
            " Ya tengo la sensación de que Jesús es divino, pero tengo algunos problemas para entender el concepto de su divinidad."
        ]
        random.shuffle(choices)
        return choices
    
     q5 = models.StringField(
        label="¿Qué opinas de la idea de que Dios ha influido y sigue influyendo en la historia de la humanidad?",
        widget=widgets.RadioSelect
    )
    def q5_choices(player):
        choices=[
            " No hay evidencia de que Dios haya intervenido alguna vez en la historia.",
            "Las personas que creyeron en Dios influyeron en la historia.",
            "Creo que la historia de la humanidad se desarrolló dentro de un orden natural que fue provocado por un poder superior.",
            "Aunque no puedo explicar quién o qué es exactamente Dios, creo que Dios tiene una influencia en la historia de la humanidad.",
            "Creo que Dios ha intervenido directa e indirectamente en la historia humana y lo sigue haciendo."
        ]
        random.shuffle(choices)
        return choices
    
     q6 = models.StringField(
        label="Creo que Dios ha intervenido directa e indirectamente en la historia humana y lo sigue haciendo.",
        widget=widgets.RadioSelect
    )
    def q6_choices(player):
        choices=[
            "La oración no es un término significativo para mí.",
            "La oración es la autoconciencia y la resolución de problemas.",
            "La oración es una meditación en la que la mente se centra en la belleza, la bondad, la comodidad, etc.",
            "En la oración, los pensamientos se dirigen a un poder superior.",
            "La oración es hablar con Dios."
        ]
        random.shuffle(choices)
        return choices
    
     q7 = models.StringField(
        label="¿Cuál de las siguientes declaraciones describe mejor su concepto de pecado?",
        widget=widgets.RadioSelect
    )
    def q7_choices(player):
        choices=[
            "No creo que exista el pecado.",
            "Creo que la gente comete errores, pero no peca.",
            "El pecado es un comportamiento que va en contra de mis propios principios personales.",
            "El pecado es un comportamiento que daña a los demás.",
            "El pecado es un comportamiento dirigido contra los principios éticos y sociales aceptados.",
            "El pecado es la imposibilidad de alcanzar los ideales espirituales más elevados que conozco."
            "El pecado es la negativa de un individuo a aceptar la voluntad de Dios para su propia vida."
        ]
        random.shuffle(choices)
        return choices
    
     q8 = models.StringField(
        label="¿Qué opina de la Biblia?",
        widget=widgets.RadioSelect
    )
    def q8_choices(player):
        choices=[
            "La Biblia es una colección de mitos y fantasías.",
            "La Biblia es una colección de escritos literarios e históricos.",
            " La Biblia contiene algunos pensamientos morales y éticos importantes de la humanidad.",
            "La Biblia fue escrita por personas inspiradas y contiene valiosas enseñanzas espirituales / espirituales.",
            "La Biblia es la palabra de Dios."
        ]
        random.shuffle(choices)
        return choices
    
     q9 = models.StringField(
        label="¿Alguna vez ha tenido una experiencia que clasificó como experiencia religiosa en ese momento? Si es así, ¿cuál de las siguientes afirmaciones se acerca más a la naturaleza predominante de su experiencia?",
        widget=widgets.RadioSelect
    )
    def q9_choices(player):
        choices=[
            "Nunca he tenido una experiencia que describiría como religiosa.",
            "No recuerdo si alguna vez tuve una experiencia que llamaría religiosa.",
            "Tuve momentos de extraordinario aprecio por la verdad, la belleza, la bondad, etc.",
            "Hubo momentos en los que fui consciente de lo divino.",
            "Tuve una experiencia (o experiencias) donde sentí un encuentro mutuo entre Dios y yo."
        ]
        random.shuffle(choices)
        return choices
    
     q10 = models.StringField(
        label="Hay momentos especiales en mi vida en los que me siento “cerca” de lo divino.",
        widget=widgets.RadioSelect
    )
    def q10_choices(player):
        choices=[
            "Fuerte aprobación",
            "Consentimiento",
            "Inseguro",
            "rechazo",
            "Fuerte rechazo"
        ]
        random.shuffle(choices)
        return choices
    
     q11 = models.StringField(
        label="Yo conozco el sentimiento de arrepentimiento y el perdon de los pecados",
        widget=widgets.RadioSelect
    )
    def q11_choices(player):
              choices=[
            "Fuerte aprobación",
            "Consentimiento",
            "Inseguro",
            "rechazo",
            "Fuerte rechazo"
        ]
        random.shuffle(choices)
        return choices
    
     q12 = models.StringField(
        label="Conozco el sentimiento de gozo y paz que proviene de darte cuenta de que eres un pecador perdonado.",
        widget=widgets.RadioSelect
    )
     def q12_choices(player):
              choices=[
            "Fuerte aprobación",
            "Consentimiento",
            "Inseguro",
            "rechazo",
            "Fuerte rechazo"
        ]
        random.shuffle(choices)
        return choices
    
      q13 = models.StringField(
        label="¿Con qué frecuencia asistes a un servicio religioso?",
        widget=widgets.RadioSelect
    )
    def q13_choices(player):
        choices=[
            "Todas las semanas.",
            "Aproximadamente dos veces al mes.",
            "Aproximadamente una vez al mes.",
            " Varias veces al año.",
            "Nunca."
        ]
        random.shuffle(choices)
        return choices
    
     q14 = models.StringField(
        label="¿Perteneces actualmente a alguna iglesia?",
        widget=widgets.RadioSelect
    )
    def q14_choices(player):
        choices=[
            "Si.",
            "No."
        ]
        random.shuffle(choices)
        return choices
    
     q15 = models.StringField(
        label="¿Dona dinero a la Iglesia?",
        widget=widgets.RadioSelect
    )
    def q15_choices(player):
        choices=[
            "Nunca.",
            "A veces.",
            "Regularmente",
            "Pago impuestos eclesiásticos."
        ]
        random.shuffle(choices)
        return choices
    
     q16 = models.StringField(
        label="¿Cómo describiría su uso de la Biblia?",
        widget=widgets.RadioSelect
    )
    def q16_choices(player):
        choices=[
            "Leo la Biblia con regularidad con fines devocionales.",
            "Leo la Biblia de manera bastante irregular, principalmente con el propósito de devoción.",
            "Leo la Biblia de vez en cuando por su enseñanza ética y moral.",
            "Leo la Biblia ocasionalmente con fines literarios o históricos.",
            "Leo la Biblia con una variedad de propósitos.",
            "Rara vez, si es que alguna vez, leo la Biblia.",
            "nunca leo la Biblia."
        ]
        random.shuffle(choices)
        return choices
     
     q17 = models.StringField(
        label="¿En cuántas organizaciones, grupos o actividades religiosas (por ejemplo, coro, grupo de jóvenes, comité, consejo, etc.) participa?",
        widget=widgets.RadioSelect
    )
    def q17_choices(player):
        choices=[
            "Ninguna.",
            "Una."
            "Dos.",
            "Tres.",
            "Cuatro.",
            "Cinco o más."
        ]
        random.shuffle(choices)
        return choices
    
     q18 = models.StringField(
        label="Dar la edad incorrecta para consumir bebidas alcohólicas es un comportamiento aceptable.",
        widget=widgets.RadioSelect
    )
     def q18_choices(player):
              choices=[
            "Fuerte aprobación",
            "Consentimiento",
            "Inseguro",
            "rechazo",
            "Fuerte rechazo"
        ]
        random.shuffle(choices)
        return choices
    
    q19 = models.StringField(
        label="No pesaría en mi conciencia si consumiera marihuana.",
        widget=widgets.RadioSelect
    )
     def q19_choices(player):
              choices=[
            "Fuerte aprobación",
            "Consentimiento",
            "Inseguro",
            "rechazo",
            "Fuerte rechazo"
        ]
        random.shuffle(choices)
        return choices
    
     q20 = models.StringField(
        label="Una relación sexual prematrimonial entre un niño y una niña que están enamorados no es inmoral",
        widget=widgets.RadioSelect
    )
    def q20_choices(player):
              choices=[
            "Fuerte aprobación",
            "Consentimiento",
            "Inseguro",
            "rechazo",
            "Fuerte rechazo"
        ]
        random.shuffle(choices)
        return choices
    
     q21 = models.StringField(
        label="Robar tapacubos o artículos pequeños en las tiendas no es inmoral",
        widget=widgets.RadioSelect
    )
     def q21_choices(player):
             choices=[
            "Fuerte aprobación",
            "Consentimiento",
            "Inseguro",
            "rechazo",
            "Fuerte rechazo"
        ]
        random.shuffle(choices)
        return choices
    
     q22 = models.StringField(
        label="La violencia puede ser una forma aceptable de protesta civil",
        widget=widgets.RadioSelect
    )
    def q22_choices(player):
          choices=[
            "Fuerte aprobación",
            "Consentimiento",
            "Inseguro",
            "rechazo",
            "Fuerte rechazo"
        ]
        random.shuffle(choices)
        return choices
    
     q23 = models.StringField(
        label="Una mujer debería poder tener un aborto independientemente de las razones para hacerlo",
        widget=widgets.RadioSelect
    )
        def q23_choices(player):
          choices=[
            "Fuerte aprobación",
            "Consentimiento",
            "Inseguro",
            "rechazo",
            "Fuerte rechazo"
        ]
        random.shuffle(choices)
        return choices
    
     q24 = models.StringField(
        label="¿Se menciona a las siguientes personas en el a) Antiguo Testamento, b) Nuevo Testamento, o c) en absoluto en la Biblia?",
        widget=widgets.RadioSelect
    )
    def q24_choices(player):
        choices=[
            "Fuerte aprobación",
            "Consentimiento",
            "Inseguro",
            "rechazo",
            "Fuerte rechazo"
        ]
        random.shuffle(choices)
        return choices
    
     q25 = models.StringField(
        label="Indique las siguientes personas mencionadas en a) el antiguo testamento b) el nuevo testamento oc) no están en la Biblia?",
        widget=widgets.RadioSelect
    )
    def q25_choices(player):
        choices=[
            "Tomás de Aquino a b c",
            "Moisés a b c",
            "Josué a b c",
            "Wesley a b c",
            "David a b c",
            "Pablo a b c",
            "Isaías a b c",
            "Lutero a b c",
            "Timoteo a b c",
            "Agustín a b c"
        ]
        random.shuffle(choices)
        return choices
    
     q26 = models.StringField(
        label="Estoy a favor de mejores viviendas para los grupos sociales desfavorecidos.",
        widget=widgets.RadioSelect
    )
    def q26_choices(player):
        choices=[
            "Fuerte aprobación",
            "Consentimiento",
            "Inseguro",
            "rechazo",
            "Fuerte rechazo"
        ]
        random.shuffle(choices)
        return choices
    
     q27 = models.StringField(
        label="Defiendo la erradicación de la pobreza en todos los sectores de la sociedad.",
        widget=widgets.RadioSelect
    )
    def q27_choices(player):
        choices=[
            "Fuerte aprobación",
            "Consentimiento",
            "Inseguro",
            "rechazo",
            "Fuerte rechazo"
        ]
        random.shuffle(choices)
        return choices
    
     q28 = models.StringField(
        label="Apoyo las oportunidades laborales completas para todos.",
        widget=widgets.RadioSelect
    )
    def q28_choices(player):
        choices=[
            "Fuerte aprobación",
            "Consentimiento",
            "Inseguro",
            "rechazo",
            "Fuerte rechazo"
        ]
        random.shuffle(choices)
        return choices
    
     q29 = models.StringField(
        label="Apoyo programas que garantizan la seguridad económica en la vejez.",
        widget=widgets.RadioSelect
    )
    def q29_choices(player):
        choices=[
           "Fuerte aprobación",
            "Consentimiento",
            "Inseguro",
            "rechazo",
            "Fuerte rechazo"
        ]
        random.shuffle(choices)
        return choices
    
     q30 = models.StringField(
        label="Creo que debería abolirse la pena de muerte.",
        widget=widgets.RadioSelect
    )
    def q30_choices(player):
        choices=[
            "Fuerte aprobación",
            "Consentimiento",
            "Inseguro",
            "rechazo",
            "Fuerte rechazo"
        ]
        random.shuffle(choices)
        return choices
    
    
     q3 = models.StringField(
        label="",
        widget=widgets.RadioSelect
    )
    def q3_choices(player):
        choices=[
            "",
            "",
            "",
            "",
            "",
            ""
        ]
        random.shuffle(choices)
        return choices
    
      q3 = models.StringField(
        label="",
        widget=widgets.RadioSelect
    )
    def q3_choices(player):
        choices=[
            "",
            "",
            "",
            "",
            "",
            ""
        ]
        random.shuffle(choices)
        return choices
    
      q3 = models.StringField(
        label="",
        widget=widgets.RadioSelect
    )
    def q3_choices(player):
        choices=[
            "",
            "",
            "",
            "",
            "",
            ""
        ]
        random.shuffle(choices)
        return choices
    
      q3 = models.StringField(
        label="",
        widget=widgets.RadioSelect
    )
    def q3_choices(player):
        choices=[
            "",
            "",
            "",
            "",
            "",
            ""
        ]
        random.shuffle(choices)
        return choices
    
      q3 = models.StringField(
        label="",
        widget=widgets.RadioSelect
    )
    def q3_choices(player):
        choices=[
            "",
            "",
            "",
            "",
            "",
            ""
        ]
        random.shuffle(choices)
        return choices
    
      q3 = models.StringField(
        label="",
        widget=widgets.RadioSelect
    )
    def q3_choices(player):
        choices=[
            "",
            "",
            "",
            "",
            "",
            ""
        ]
        random.shuffle(choices)
        return choices
    
      q3 = models.StringField(
        label="",
        widget=widgets.RadioSelect
    )
    def q3_choices(player):
        choices=[
            "",
            "",
            "",
            "",
            "",
            ""
        ]
        random.shuffle(choices)
        return choices
    
      q3 = models.StringField(
        label="",
        widget=widgets.RadioSelect
    )
    def q3_choices(player):
        choices=[
            "",
            "",
            "",
            "",
            "",
            ""
        ]
        random.shuffle(choices)
        return choices
    
      q3 = models.StringField(
        label="",
        widget=widgets.RadioSelect
    )
    def q3_choices(player):
        choices=[
            "",
            "",
            "",
            "",
            "",
            ""
        ]
        random.shuffle(choices)
        return choices
    
      q3 = models.StringField(
        label="",
        widget=widgets.RadioSelect
    )
    def q3_choices(player):
        choices=[
            "",
            "",
            "",
            "",
            "",
            ""
        ]
        random.shuffle(choices)
        return choices
    
      q3 = models.StringField(
        label="",
        widget=widgets.RadioSelect
    )
    def q3_choices(player):
        choices=[
            "",
            "",
            "",
            "",
            "",
            ""
        ]
        random.shuffle(choices)
        return choices
    
      q3 = models.StringField(
        label="",
        widget=widgets.RadioSelect
    )
    def q3_choices(player):
        choices=[
            "",
            "",
            "",
            "",
            "",
            ""
        ]
        random.shuffle(choices)
        return choices
    
      q3 = models.StringField(
        label="",
        widget=widgets.RadioSelect
    )
    def q3_choices(player):
        choices=[
            "",
            "",
            "",
            "",
            "",
            ""
        ]
        random.shuffle(choices)
        return choices
    
      q3 = models.StringField(
        label="",
        widget=widgets.RadioSelect
    )
    def q3_choices(player):
        choices=[
            "",
            "",
            "",
            "",
            "",
            ""
        ]
        random.shuffle(choices)
        return choices
    
      q3 = models.StringField(
        label="",
        widget=widgets.RadioSelect
    )
    def q3_choices(player):
        choices=[
            "",
            "",
            "",
            "",
            "",
            ""
        ]
        random.shuffle(choices)
        return choices
    
      q3 = models.StringField(
        label="",
        widget=widgets.RadioSelect
    )
    def q3_choices(player):
        choices=[
            "",
            "",
            "",
            "",
            "",
            ""
        ]
        random.shuffle(choices)
        return choices
    
      q3 = models.StringField(
        label="",
        widget=widgets.RadioSelect
    )
    def q3_choices(player):
        choices=[
            "",
            "",
            "",
            "",
            "",
            ""
        ]
        random.shuffle(choices)
        return choices
    
      q3 = models.StringField(
        label="",
        widget=widgets.RadioSelect
    )
    def q3_choices(player):
        choices=[
            "",
            "",
            "",
            "",
            "",
            ""
        ]
        random.shuffle(choices)
        return choices
    
      q3 = models.StringField(
        label="",
        widget=widgets.RadioSelect
    )
    def q3_choices(player):
        choices=[
            "",
            "",
            "",
            "",
            "",
            ""
        ]
        random.shuffle(choices)
        return choices
    
    
     q3 = models.StringField(
        label="",
        widget=widgets.RadioSelect
    )
    def q3_choices(player):
        choices=[
            "",
            "",
            "",
            "",
            "",
            ""
        ]
        random.shuffle(choices)
        return choices
    
      q3 = models.StringField(
        label="",
        widget=widgets.RadioSelect
    )
    def q3_choices(player):
        choices=[
            "",
            "",
            "",
            "",
            "",
            ""
        ]
        random.shuffle(choices)
        return choices
    
      q3 = models.StringField(
        label="",
        widget=widgets.RadioSelect
    )
    def q3_choices(player):
        choices=[
            "",
            "",
            "",
            "",
            "",
            ""
        ]
        random.shuffle(choices)
        return choices
    
      q3 = models.StringField(
        label="",
        widget=widgets.RadioSelect
    )
    def q3_choices(player):
        choices=[
            "",
            "",
            "",
            "",
            "",
            ""
        ]
        random.shuffle(choices)
        return choices
    
      q3 = models.StringField(
        label="",
        widget=widgets.RadioSelect
    )
    def q3_choices(player):
        choices=[
            "",
            "",
            "",
            "",
            "",
            ""
        ]
        random.shuffle(choices)
        return choices
    
      q3 = models.StringField(
        label="",
        widget=widgets.RadioSelect
    )
    def q3_choices(player):
        choices=[
            "",
            "",
            "",
            "",
            "",
            ""
        ]
        random.shuffle(choices)
        return choices
    
      q3 = models.StringField(
        label="",
        widget=widgets.RadioSelect
    )
    def q3_choices(player):
        choices=[
            "",
            "",
            "",
            "",
            "",
            ""
        ]
        random.shuffle(choices)
        return choices
    
      q3 = models.StringField(
        label="",
        widget=widgets.RadioSelect
    )
    def q3_choices(player):
        choices=[
            "",
            "",
            "",
            "",
            "",
            ""
        ]
        random.shuffle(choices)
        return choices
    
      q3 = models.StringField(
        label="",
        widget=widgets.RadioSelect
    )
    def q3_choices(player):
        choices=[
            "",
            "",
            "",
            "",
            "",
            ""
        ]
        random.shuffle(choices)
        return choices
    
      q3 = models.StringField(
        label="",
        widget=widgets.RadioSelect
    )
    def q3_choices(player):
        choices=[
            "",
            "",
            "",
            "",
            "",
            ""
        ]
        random.shuffle(choices)
        return choices
    
      q3 = models.StringField(
        label="",
        widget=widgets.RadioSelect
    )
    def q3_choices(player):
        choices=[
            "",
            "",
            "",
            "",
            "",
            ""
        ]
        random.shuffle(choices)
        return choices
    
      q3 = models.StringField(
        label="",
        widget=widgets.RadioSelect
    )
    def q3_choices(player):
        choices=[
            "",
            "",
            "",
            "",
            "",
            ""
        ]
        random.shuffle(choices)
        return choices
    
      q3 = models.StringField(
        label="",
        widget=widgets.RadioSelect
    )
    def q3_choices(player):
        choices=[
            "",
            "",
            "",
            "",
            "",
            ""
        ]
        random.shuffle(choices)
        return choices
    
      q3 = models.StringField(
        label="",
        widget=widgets.RadioSelect
    )
    def q3_choices(player):
        choices=[
            "",
            "",
            "",
            "",
            "",
            ""
        ]
        random.shuffle(choices)
        return choices
    
      q3 = models.StringField(
        label="",
        widget=widgets.RadioSelect
    )
    def q3_choices(player):
        choices=[
            "",
            "",
            "",
            "",
            "",
            ""
        ]
        random.shuffle(choices)
        return choices
    
      q3 = models.StringField(
        label="",
        widget=widgets.RadioSelect
    )
    def q3_choices(player):
        choices=[
            "",
            "",
            "",
            "",
            "",
            ""
        ]
        random.shuffle(choices)
        return choices
    
      q3 = models.StringField(
        label="",
        widget=widgets.RadioSelect
    )
    def q3_choices(player):
        choices=[
            "",
            "",
            "",
            "",
            "",
            ""
        ]
        random.shuffle(choices)
        return choices
    
      q3 = models.StringField(
        label="",
        widget=widgets.RadioSelect
    )
    def q3_choices(player):
        choices=[
            "",
            "",
            "",
            "",
            "",
            ""
        ]
        random.shuffle(choices)
        return choices
    
      q3 = models.StringField(
        label="",
        widget=widgets.RadioSelect
    )
    def q3_choices(player):
        choices=[
            "",
            "",
            "",
            "",
            "",
            ""
        ]
        random.shuffle(choices)
        return choices
    
      q3 = models.StringField(
        label="",
        widget=widgets.RadioSelect
    )
    def q3_choices(player):
        choices=[
            "",
            "",
            "",
            "",
            "",
            ""
        ]
        random.shuffle(choices)
        return choices
    
      q3 = models.StringField(
        label="",
        widget=widgets.RadioSelect
    )
    def q3_choices(player):
        choices=[
            "",
            "",
            "",
            "",
            "",
            ""
        ]
        random.shuffle(choices)
        return choices
    
      q3 = models.StringField(
        label="",
        widget=widgets.RadioSelect
    )
    def q3_choices(player):
        choices=[
            "",
            "",
            "",
            "",
            "",
            ""
        ]
        random.shuffle(choices)
        return choices
    
      q3 = models.StringField(
        label="",
        widget=widgets.RadioSelect
    )
    def q3_choices(player):
        choices=[
            "",
            "",
            "",
            "",
            "",
            ""
        ]
        random.shuffle(choices)
        return choices
    
      q3 = models.StringField(
        label="",
        widget=widgets.RadioSelect
    )
    def q3_choices(player):
        choices=[
            "",
            "",
            "",
            "",
            "",
            ""
        ]
        random.shuffle(choices)
        return choices
    
      q3 = models.StringField(
        label="",
        widget=widgets.RadioSelect
    )
    def q3_choices(player):
        choices=[
            "",
            "",
            "",
            "",
            "",
            ""
        ]
        random.shuffle(choices)
        return choices
    
      q3 = models.StringField(
        label="",
        widget=widgets.RadioSelect
    )
    def q3_choices(player):
        choices=[
            "",
            "",
            "",
            "",
            "",
            ""
        ]
        random.shuffle(choices)
        return choices
    
      q3 = models.StringField(
        label="",
        widget=widgets.RadioSelect
    )
    def q3_choices(player):
        choices=[
            "",
            "",
            "",
            "",
            "",
            ""
        ]
        random.shuffle(choices)
        return choices
    
      q3 = models.StringField(
        label="",
        widget=widgets.RadioSelect
    )
    def q3_choices(player):
        choices=[
            "",
            "",
            "",
            "",
            "",
            ""
        ]
        random.shuffle(choices)
        return choices
    
      q3 = models.StringField(
        label="",
        widget=widgets.RadioSelect
    )
    def q3_choices(player):
        choices=[
            "",
            "",
            "",
            "",
            "",
            ""
        ]
        random.shuffle(choices)
        return choices
    
    q3 = models.StringField(
        label="",
        widget=widgets.RadioSelect
    )
    def q3_choices(player):
        choices=[
            "",
            "",
            "",
            "",
            "",
            ""
        ]
        random.shuffle(choices)
        return choices
    
    q3 = models.StringField(
        label="",
        widget=widgets.RadioSelect
    )
    def q3_choices(player):
        choices=[
            "",
            "",
            "",
            "",
            "",
            ""
        ]
        random.shuffle(choices)
        return choices
    
    q3 = models.StringField(
        label="",
        widget=widgets.RadioSelect
    )
    def q3_choices(player):
        choices=[
            "",
            "",
            "",
            "",
            "",
            ""
        ]
        random.shuffle(choices)
        return choices
    
    q3 = models.StringField(
        label="",
        widget=widgets.RadioSelect
    )
    def q3_choices(player):
        choices=[
            "",
            "",
            "",
            "",
            "",
            ""
        ]
        random.shuffle(choices)
        return choices
    
    q3 = models.StringField(
        label="",
        widget=widgets.RadioSelect
    )
    def q3_choices(player):
        choices=[
            "",
            "",
            "",
            "",
            "",
            ""
        ]
        random.shuffle(choices)
        return choices
    
    q3 = models.StringField(
        label="",
        widget=widgets.RadioSelect
    )
    def q3_choices(player):
        choices=[
            "",
            "",
            "",
            "",
            "",
            ""
        ]
        random.shuffle(choices)
        return choices
    
    q3 = models.StringField(
        label="",
        widget=widgets.RadioSelect
    )
    def q3_choices(player):
        choices=[
            "",
            "",
            "",
            "",
            "",
            ""
        ]
        random.shuffle(choices)
        return choices
    
   q3 = models.StringField(
        label="",
        widget=widgets.RadioSelect
    )
    def q3_choices(player):
        choices=[
            "",
            "",
            "",
            "",
            "",
            ""
        ]
        random.shuffle(choices)
        return choices
    
    q3 = models.StringField(
        label="",
        widget=widgets.RadioSelect
    )
    def q3_choices(player):
        choices=[
            "",
            "",
            "",
            "",
            "",
            ""
        ]
        random.shuffle(choices)
        return choices
    
    
    q3 = models.StringField(
        label="",
        widget=widgets.RadioSelect
    )
    def q3_choices(player):
        choices=[
            "",
            "",
            "",
            "",
            "",
            ""
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

