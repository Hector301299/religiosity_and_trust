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
    
    
     q31 = models.StringField(
        label="¿Cuál es tu actitud hacia la fama?",
        widget=widgets.RadioSelect
    )
    def q31_choices(player):
        choices=[
            "Me gustaría ser famoso si eso me hace rico.",
            "Me gustaría ser famoso aunque eso no me haga rico.",
            "Me gustaría ser famoso siempre que no perturbe mi privacidad.",
            "Prefiero no ser famoso."
        ]
        random.shuffle(choices)
        return choices
    
      q32 = models.StringField(
        label="En su opinión, ¿cuál es el papel de un gobierno (marque todas las opciones que correspondan)?",
        widget=widgets.RadioSelect
    )
    def q32_choices(player):
        choices=[
            "Infraestructura del edificio.",
            "Hacer cumplir las leyes.",
            "Regulación de la economía.",
            "Defensa nacional."
        ]
        random.shuffle(choices)
        return choices
    
      q33 = models.StringField(
        label="¿Cómo se siente al tener poder político?",
        widget=widgets.RadioSelect
    )
    def q33_choices(player):
        choices=[
            "Esto me permite mejorar la calidad de vida de los demás.",
            "Esto implica demasiada responsabilidad y no lo aceptaría.",
            "Esto me permite lograr mis objetivos políticos.",
            "No sé mucho de política y no me importa.",
            "Es un negocio sucio y me apasiona tener poder político."
        ]Es un negocio sucio y me apasiona tener poder político.
        random.shuffle(choices)
        return choices
    
      q34 = models.StringField(
        label="¿Cómo te sientes acerca de poseer riquezas?",
        widget=widgets.RadioSelect
    )
    def q34_choices(player):
        choices=[
            "Esto me da más libertad para hacer lo que quiero hacer.",
            "Esto me limita demasiado y no puedo llevar una vida normal.",
            "Eso no necesariamente me hace sentir mejor.",
            "Seguramente mejorará la vida.",
            "Esto es solo una preocupación y no creo que valga la pena."
        ]
        random.shuffle(choices)
        return choices
    
      q35 = models.StringField(
        label="¿Qué parte del periódico es más importante para ti?",
        widget=widgets.RadioSelect
    )
    def q35_choices(player):
        choices=[
            "Finanzas / Economía.",
            "Noticias locales.",
            "Noticias regionales.",
            "Noticias mundiales.",
            "Deporte.",
            "Estilo de vida."
        ]
        random.shuffle(choices)
        return choices
    
      q36 = models.StringField(
        label="¿Cuál es su actitud hacia la protección del medio ambiente?",
        widget=widgets.RadioSelect
    )
    def q36_choices(player):
        choices=[
            "Esa no es nuestra responsabilidad.",
            "Solo somos responsables como un solo individuo de no destruir la naturaleza.",
            "Tenemos la responsabilidad de las generaciones futuras y, por tanto, deberíamos prestarle más atención.",
            "Esto solo tiene sentido si los beneficios económicos superan los costos.",
            "No me importa en absoluto.",
        ]
        random.shuffle(choices)
        return choices
    
      q37 = models.StringField(
        label="¿Qué opinas de los animales?",
        widget=widgets.RadioSelect
    )
    def q37_choices(player):
        choices=[
            "Son seres subordinados a los humanos y nosotros podemos decidir su destino.",
            "Deben ser respetados y no asesinados por comer o hacer ejercicio.",
            "Debemos comportarnos bien con ellos, pero los animales se pueden comer.",
            "Son nuestros iguales y deben ser tratados como tales."
        ]
        random.shuffle(choices)
        return choices
    
      q38 = models.StringField(
        label="¿Cuál es su uso principal de los periódicos?",
        widget=widgets.RadioSelect
    )
    def q38_choices(player):
        choices=[
            "Los leo para obtener información sobre los últimos acontecimientos.",
            "Obtener nuevas opiniones.",
            "Para relajarse.",
            "a y b",
            "b y c",
            "a y c"
        ]
        random.shuffle(choices)
        return choices
    
      q39 = models.StringField(
        label="¿Qué tipo de gobierno cree que representa el mejor liderazgo político?",
        widget=widgets.RadioSelect
    )
    def q39_choices(player):
        choices=[
            "Cualquier dictadura",
            "Dictadura benévola",
            "Democracia autoritaria",
            "Democracia pura",
            "Anarquía"
        ]
        random.shuffle(choices)
        return choices
   
    
      q40 = models.StringField(
        label="¿Cuál es su opinión sobre el sistema de depósito?",
        widget=widgets.RadioSelect
    )
    def q40_choices(player):
        choices=[
            "Económicamente ineficaz y una pérdida de tiempo.",
            "Económicamente ineficiente pero valioso para el medio ambiente.",
            "Económicamente eficiente y valioso para el medio ambiente."
        ]
        random.shuffle(choices)
        return choices
    
      q41 = models.StringField(
        label="¿Cuánto deberían el gobierno y la gente comunicarse entre sí?",
        widget=widgets.RadioSelect
    )
    def q41_choices(player):
        choices=[
            "No puedo molestarme en comunicarme con mi gobierno.",
            "Es importante, pero imposible, que el gobierno y las personas se comuniquen libremente entre sí.",
            "Es importante para la conexión mutua y la coherencia en todos los niveles.",
            "Es importante, pero solo en una dirección, es decir, informar a la gente a través del gobierno.",
            "Es importante que el gobierno sepa lo que quiere la gente, pero tiene la autoridad para tomar las decisiones en última instancia."
        ]
        random.shuffle(choices)
        return choices
    
      q42 = models.StringField(
        label="¿Cuál es su deporte favorito?",
        widget=widgets.RadioSelect
    )
    def q42_choices(player):
        choices=[
            "Deportes para espectadores.",
            "Deportes de equipo.",
            "Deportes individuales.",
            "Cualquier deporte sin violencia.",
            "Deportes que impliquen violencia."
        ]
        random.shuffle(choices)
        return choices
    
      q43 = models.StringField(
        label="¿Cómo define democracia?",
        widget=widgets.RadioSelect
    )
    def q43_choices(player):
        choices=[
            "Un sistema en el que todo el liderazgo es elegido por el pueblo.",
            "Un sistema en el que todos puedan hablar libremente.",
            "Un sistema en el que la legislación y la política son elegidas por el pueblo.",
            "a y b",
            "b y c",
            "a, b y c"
        ]
        random.shuffle(choices)
        return choices
    
      q44 = models.StringField(
        label="¿Cómo define el crimen?",
        widget=widgets.RadioSelect
    )
    def q44_choices(player):
        choices=[
            "Todo acto que atente contra la libertad de otra persona.",
            "Cualquier acto tipificado como delito en la legislación de mi país.",
            "Cualquier acto que esté tipificado como delito según la ley del país en el que me encuentre actualmente.",
            "Cualquier acción que me haga sentir que no soy bueno para mí.",
            "No hay delitos, solo depende de las definiciones sociales."
        ]
        random.shuffle(choices)
        return choices
    
      q45 = models.StringField(
        label="En primer lugar, ¿cuál es su actitud hacia la guerra?",
        widget=widgets.RadioSelect
    )
    def q45_choices(player):
        choices=[
            "La guerra es necesaria para mantener la soberanía.",
            "La amenaza de guerra ayuda a mantener la paz.",
            "La guerra cuesta vidas humanas y debe prohibirse.",
            "La guerra es una forma de autodefensa.",
            "La guerra es solo una forma arrogante de presentar el propio poder."
        ]
        random.shuffle(choices)
        return choices
    
      q46 = models.StringField(
        label="Me siento mejor cuando una tarea que hay que hacer es difícil.",
        widget=widgets.RadioSelect
    )
    def q46_choices(player):
        choices=[
            "Fuerte aprobación",
            "Consentimiento",
            "Inseguro",
            "Rechazo",
            "Fuerte rechazo"
        ]
        random.shuffle(choices)
        return choices
    
      q47 = models.StringField(
        label="A menudo he temido que mi libertad personal se vea amenazada por un cambio de gobierno.",
        widget=widgets.RadioSelect
    )
    def q47_choices(player):
        choices=[
           "Fuerte aprobación",
            "Consentimiento",
            "Inseguro",
            "Rechazo",
            "Fuerte rechazo"
        ]
        random.shuffle(choices)
        return choices
    
      q48 = models.StringField(
        label="A veces siento que la influencia de la política en la educación y la enseñanza es negativa y fuerte.",
        widget=widgets.RadioSelect
    )
    def q48_choices(player):
        choices=[
            "Fuerte aprobación",
            "Consentimiento",
            "Inseguro",
            "Rechazo",
            "Fuerte rechazo"
        ]
        random.shuffle(choices)
        return choices
    
    
     q49 = models.StringField(
        label="Prefiero estar en la naturaleza a ir de compras cuando busco entretenimiento / diversión.",
        widget=widgets.RadioSelect
    )
    def q49_choices(player):
        choices=[
            "Fuerte aprobación",
            "Consentimiento",
            "Inseguro",
            "Rechazo",
            "Fuerte rechazo"
        ]
        random.shuffle(choices)
        return choices
    
      q50 = models.StringField(
        label="Hay momentos especiales en mi vida en los que me siento muy cerca de mi familia y amigos.",
        widget=widgets.RadioSelect
    )
    def 50_choices(player):
        choices=[
            "Fuerte aprobación",
            "Consentimiento",
            "Inseguro",
            "Rechazo",
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
    
    
    
    
#    ed = models.BooleanField(
#        label="Are you left
# -handed?",
#        choices=[
#            [True,"Yes"],[False,"No"],
#        ]
#    )

