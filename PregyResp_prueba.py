
# Juego de Preguntas y Respuestas sobre Mujeres en la Música


#importar librerias
import random
import time


#Diccionario de preguntas y respuestas fáciles
preguntas_opciones_facil= {
    "¿Quién fue la primera mujer en entrar al Salón de la Fama del Rock and Roll?\n"
    "A) Aretha Franklin\n"
    "B) Janis Joplin\n"
    "C) Tina Turner\n"
    "D) Patti Smith": "A",
    "¿Quién es la artista femenina más escuchada en la historia de Spotify (hasta 2023)?\n"
    "A) Taylor Swift\n"
    "B) Ariana Grande\n"
    "C) Billie Eilish\n"
    "D) Rihanna": "A",
    "¿Qué cantante interpreta la canción `All I Want for Christmas Is You`?\n"
    "A) Nicki Minaj\n"
    "B) Celine Dion\n"
    "C) Mariah Carey\n"
    "D) Whitney Houston": "C",
    "¿Qué cantante chilena es conocida por su canción `Tu falta de querer` y su estilo emocional y desgarrador?\n"
    "A) Ana Tijoux\n"
    "B) Mon Laferte\n"
    "C) Denise Rosenthal\n"
    "D) Francisca Valenzuela": "B",
    "¿Qué cantante fue la primera mujer negra en ganar un Oscar a la mejor actriz?\n"
    "A) Diana Ross\n"
    "B) Jennifer Hudson\n"
    "C) Whitney Houston\n"
    "D) Halle Berry": "D",
    "¿Qué artista española ganó el Grammy Latino a Mejor Nuevo Artista en 2022?\n"
    "A) Rigoberta Bandini\n"
    "B) Guitarricadelafuente\n"
    "C) Rosalía\n"
    "D) Silvana Estrada": "D",
    "¿Qué artista latina es conocida como 'La Reina del Tex-Mex'?\n"
    "A) Paulina Rubio\n"
    "B) Selena Quintanilla\n"
    "C) Thalía\n"
    "D) Jenni Rivera": "B",
    "¿Qué artista pop se hizo famosa por su estética pin-up y canciones como `I Kissed a Girl`?\n"
    "A) Lady Gaga\n"
    "B) Katy Perry\n"
    "C) Meghan Trainor\n"
    "D) Christina Aguilera": "B",
    "¿Quién es la cantante de flamenco-pop que popularizó el tema `Tú me dejaste de querer` junto a C. Tangana?\n"
    "A) Rosalía\n"
    "B) La Húngara\n"
    "C) India Martínez\n"
    "D) Mala Rodríguez": "B",
    "¿Qué mujer es considerada una de las pioneras del punk rock con su banda The Slits?\n"
    "A) Debbie Harry\n"
    "B) Siouxsie Sioux\n"
    "C) Ari Up\n"
    "D) Joan Jett": "C",
    "¿Qué pionera del jazz es conocida como `La Primera Dama de la Canción`?\n"
    "A) Billie Holiday\n"
    "B) Ella Fitzgerald\n"
    "C) Nina Simone\n"
    "D) Sarah Vaughan": "B",
    "¿Qué artista es conocida por su estética futurista y su sencillo `Say So`?\n"
    "A) SZA\n"
    "B) Doja Cat\n"
    "C) Megan Thee Stallion\n"
    "D) Normani": "B",
    "¿Qué cantante afroamericana es considerada un ícono del soul y del activismo por los derechos civiles?\n"
    "A) Aretha Franklin\n"
    "B) Nina Simone\n"
    "C) Diana Ross\n"
    "D) Whitney Houston": "B",
    "¿Qué artista argentina ganó reconocimiento mundial con su sencillo `Disciplina` y su álbum `Cupido`?\n"
    "A) TINI\n"
    "B) Cazzu\n"
    "C) Nathy Peluso\n"
    "D) Lali": "D",
    "¿Qué cantante lanzó el exitoso tema “good 4 u”, convirtiéndose en una de las mayores revelaciones del pop en 2021?\n"
    "A) Billie Eilish\n"
    "B) Olivia Rodrigo\n"
    "C) Sabrina Carpenter\n"
    "D) Tate McRae": "B",
    "¿Qué cantante fue la primera mujer afroamericana en ser cabeza de cartel en el festival Coachella (2018)?\n"
    "A) Nicki Minaj\n"
    "B) Rihanna\n"
    "C) Beyoncé\n"
    "D) SZA": "C",
    "¿Qué artista lanzó el álbum “Born to Die” y es conocida por su estilo melancólico y cinematográfico?\n"
    "A) Lorde\n"
    "B) Lana Del Rey\n"
    "C) Norah Jones\n"
    "D) Jorja Smith": "B",
    "¿Quién es la cantante que interpretó “Truth Hurts” y promueve el empoderamiento y la aceptación corporal a través de su música?\n"
    "A) Cardi B\n"
    "B) Lizzo\n"
    "C) Megan Thee Stallion\n"
    "D) Doja Cat": "B",
    "¿Qué cantante fue la primera mujer en ganar el Latin Grammy a la Persona del Año (en 2011)?\n"
    "A) Gloria Estefan\n"
    "B) Mercedes Sosa\n"
    "C) Shakira\n"
    "D) Celia Cruz": "B",
    "¿Quién fue la cantante más joven en debutar en el número 1 del Billboard Hot 100 con su primer sencillo “Your Love”?\n"
    "A) Doja Cat\n"
    "B) Nicki Minaj\n"
    "C) Britney Spears\n"
    "D) Cardi B": "B",
    "¿Qué cantante ganó el Grammy a Mejor Álbum Pop Vocal en 2019 por “Sweetener”?\n"
    "A) Ariana Grande\n"
    "B) Lady Gaga\n"
    "C) Dua Lipa\n"
    "D) Taylor Swift": "A",
    "¿Qué cantante estadounidense es conocida por sus potentes presentaciones en vivo y el himno “Just Give Me a Reason”?\n"
    "A) Adele\n"
    "B) P!nk\n"
    "C) Christina Aguilera\n"
    "D) Kelly Clarkson": "B",
    "¿Quién fue la artista más escuchada en Spotify en 2024 por segundo año consecutivo?\n"
    "A) Billie Eilish\n"
    "B) Dua Lipa\n"
    "C) Taylor Swift\n"
    "D) Olivia Rodrigo": "C",
    "¿Qué canción fue la más escuchada a nivel mundial en 2024?\n"
    "A) Flowers\n"
    "B) Espresso\n"
    "C) Anti-Hero\n"
    "D) Despechá": "B",
    "¿De quién es la canción del baile viral de la serie 'Wednesday' (Merlina)?\n"
    "A) Doja Cat\n"
    "B) Billie Eilish\n"
    "C) Lady Gaga\n"
    "D) Megan Thee Stallion": "C",
    "¿Cómo se llama el álbum de Rosalía que revolucionó el mundo de la música?\n"
    "A) El Mal Querer\n"
    "B) Motomami\n"
    "C) Saoko\n"
    "D) Linda": "B",
    "¿De qué cantante son los siguientes temas: “Suerte”, “Inevitable”, “La Tortura”?\n"
    "A) Shakira\n"
    "B) Paulina Rubio\n"
    "C) Thalía\n"
    "D) Ana Gabriel": "A",
    "¿Qué cantante y actriz ganó su primer Grammy por el tema “Flowers”?\n"
    "A) Miley Cyrus\n"
    "B) Selena Gomez\n"
    "C) Demi Lovato\n"
    "D) Sabrina Carpenter": "A",
    "¿Qué artista comenzó subiendo temas a SoundCloud con su hermano, destacando con “Ocean Eyes”?\n"
    "A) Billie Eilish\n"
    "B) Olivia Rodrigo\n"
    "C) Lorde\n"
    "D) Gracie Abrams": "A",
    "¿Quiénes son consideradas la reina y la princesa del pop mundial?\n"
    "A) Madonna y Britney Spears\n"
    "B) Beyoncé y Rihanna\n"
    "C) Mariah Carey y Ariana Grande\n"
    "D) Lady Gaga y Taylor Swift": "A",
    "¿Qué gira ha sido la más lucrativa de la historia, con una recaudación de $2 mil millones?\n"
    "A) Renaissance World Tour\n"
    "B) Future Nostalgia Tour\n"
    "C) The Eras Tour\n"
    "D) Chromatica Ball": "C",
    "¿Cuál es considerado el grupo de chicas más popular de todos los tiempos?\n"
    "A) Destiny’s Child\n"
    "B) Spice Girls\n"
    "C) BLACKPINK\n"
    "D) Little Mix": "B",
    "¿Qué artista fue la primera en llenar el Estadio Santiago Bernabéu de Madrid cuatro veces consecutivas?\n"
    "A) Rosalía\n"
    "B) Karol G\n"
    "C) Shakira\n"
    "D) Aitana": "B",
    "¿Qué cantante lanzó el icónico álbum \"Jagged Little Pill\", que incluye temas como \"You Oughta Know\" y \"Ironic\"?\n"
    "A) Alanis Morissette\n"
    "B) Avril Lavigne\n"
    "C) Fiona Apple\n"
    "D) Jewel": "A",
    "¿Quién es la vocalista principal de la banda Paramore, conocida por temas como \"Misery Business\" y \"Still Into You\"?\n"
    "A) Hayley Williams\n"
    "B) Gwen Stefani\n"
    "C) Florence Welch\n"
    "D) Amy Lee": "A",
    "¿Qué artista lanzó en 2023 el álbum “The Rise and Fall of a Midwest Princess” y fue considerada una revelación del pop alternativo?\n"
    "A) Chappell Roan\n"
    "B) Tate McRae\n"
    "C) Gracie Abrams\n"
    "D) Maggie Rogers": "A",
    "¿Qué grupo femenino surcoreano lanzó el hit “How You Like That” y ha sido uno de los máximos exponentes del K-pop mundial?\n"
    "A) Red Velvet\n"
    "B) BLACKPINK\n"
    "C) Twice\n"
    "D) NewJeans": "B"
}


#Diccionario de preguntas y respuestas difíciles
preguntas_respuestas_dificil = {
    "¿Qué cantante fue la primera mujer en ganar el Latin Grammy a la Persona del Año (en 2011)?": "Mercedes Sosa",
    "¿Quién fue la cantante más joven en debutar en el número 1 del Billboard Hot 100 con su primer sencillo “Your Love”?": "Nicki Minaj",
    "¿Qué cantante ganó el Grammy a Mejor Álbum Pop Vocal en 2019 por “Sweetener”?": "Ariana Grande",
    "¿Qué cantante estadounidense es conocida por sus potentes presentaciones en vivo y el himno “Just Give Me a Reason”?": "Pink",
    "¿Quién fue la artista más escuchada en Spotify en 2024 por segundo año consecutivo?": "Taylor Swift",
    "¿Qué canción fue la más escuchada a nivel mundial en 2024?": "Espresso",
    "¿De quién es la canción del baile viral de la serie 'Wednesday' (Merlina)?": "Lady Gaga",
    "¿Cómo se llama el álbum de Rosalía que revolucionó el mundo de la música?": "Motomami",
    "¿De qué cantante son los siguientes temas: “Suerte”, “Inevitable”, “La Tortura”?": "Shakira",
    "¿Qué cantante y actriz ganó su primer Grammy por el tema “Flowers”?": "Miley Cyrus",
    "¿Qué artista comenzó subiendo temas a SoundCloud con su hermano, destacando con “Ocean Eyes”?": "Billie Eilish",
    "¿Quiénes son consideradas la reina y la princesa del pop mundial?": "Madonna y Britney Spears",
    "¿Qué gira ha sido la más lucrativa de la historia, con una recaudación de $2 mil millones?": "The Eras Tour",
    "¿Cuál es considerado el grupo de chicas más popular de todos los tiempos?": "Spice Girls",
    "¿Qué artista fue la primera en llenar el Estadio Santiago Bernabéu de Madrid cuatro veces consecutivas?": "Karol G",
    "¿Qué cantante lanzó el icónico álbum \"Jagged Little Pill\", que incluye temas como \"You Oughta Know\" y \"Ironic\"?": "Alanis Morissette",
    "¿Quién es la vocalista principal de la banda Paramore, conocida por temas como \"Misery Business\" y \"Still Into You\"?": "Hayley Williams",
    "¿Qué artista lanzó en 2023 el álbum “The Rise and Fall of a Midwest Princess” y fue considerada una revelación del pop alternativo?": "Chappell Roan",
    "¿Qué grupo femenino surcoreano lanzó el hit “How You Like That” y ha sido uno de los máximos exponentes del K-pop mundial?": "BLACKPINK",
    "¿Quién es la cantante que interpretó “Truth Hurts” y promueve el empoderamiento y la aceptación corporal a través de su música?": "Lizzo",
    "¿Qué artista lanzó el álbum “Born to Die” y es conocida por su estilo melancólico y cinematográfico?": "Lana Del Rey",
    "¿Qué cantante fue la primera mujer afroamericana en ser cabeza de cartel en el festival Coachella (2018)?": "Beyoncé",
    "¿Qué cantante lanzó el exitoso tema “good 4 u”, convirtiéndose en una de las mayores revelaciones del pop en 2021?": "Olivia Rodrigo",
    "¿Quién fue la primera mujer en entrar al Salón de la Fama del Rock and Roll?": "Aretha Franklin",
    "¿Quién es la artista femenina más escuchada en la historia de Spotify (hasta 2023)?": "Taylor Swift",
    "¿Qué cantante interpreta la canción `All I Want for Christmas Is You`?": "Mariah Carey",
    "¿Qué cantante chilena es conocida por su canción `Tu falta de querer` y su estilo emocional y desgarrador?": "Mon Laferte",
    "¿Qué cantante fue la primera mujer negra en ganar un Oscar a la mejor actriz?": "Halle Berry",
    "¿Qué artista española ganó el Grammy Latino a Mejor Nuevo Artista en 2022?": "Silvana Estrada",
    "¿Qué artista latina es conocida como 'La Reina del Tex-Mex'?": "Selena Quintanilla",
    "¿Qué artista pop se hizo famosa por su estética pin-up y canciones como `I Kissed a Girl`?": "Katy Perry",
    "¿Quién es la cantante de flamenco-pop que popularizó el tema `Tú me dejaste de querer` junto a C. Tangana?": "La Húngara",
    "¿Qué mujer es considerada una de las pioneras del punk rock con su banda The Slits?": "Ari Up",
    "¿Qué pionera del jazz es conocida como `La Primera Dama de la Canción`?": "Ella Fitzgerald",
    "¿Qué artista es conocida por su estética futurista y su sencillo `Say So`?": "Doja Cat",
    "¿Qué cantante afroamericana es considerada un ícono del soul y del activismo por los derechos civiles?": "Nina Simone",
    "¿Qué artista argentina ganó reconocimiento mundial con su sencillo `Disciplina` y su álbum `Cupido`?": "Lali"
}

#FUNCIONES

#Mensaje de Bienvenida
def mostrar_mensaje_bienvenida():

    print("¡Bienvenido al Juego de Preguntas y Respuestas!")
    print("\033[96m")  # Cambia el color del texto a cian
    print(""" 
    ███    ███ ██    ██      ██ ███████ ██████  ███████ ███████     ███████ ███    ██     ██       █████      ███    ███ ██    ██ ███████ ██  ██████  █████  
    ████  ████ ██    ██      ██ ██      ██   ██ ██      ██          ██      ████   ██     ██      ██   ██     ████  ████ ██    ██ ██      ██ ██      ██   ██ 
    ██ ████ ██ ██    ██      ██ █████   ██████  █████   ███████     █████   ██ ██  ██     ██      ███████     ██ ████ ██ ██    ██ ███████ ██ ██      ███████ 
    ██  ██  ██ ██    ██ ██   ██ ██      ██   ██ ██           ██     ██      ██  ██ ██     ██      ██   ██     ██  ██  ██ ██    ██      ██ ██ ██      ██   ██ 
    ██      ██  ██████   █████  ███████ ██   ██ ███████ ███████     ███████ ██   ████     ███████ ██   ██     ██      ██  ██████  ███████ ██  ██████ ██   ██ 
    """)
    print("\033[0m")  # Reset color
    
    print("\033[1m Reglas del juego:\033[0m")
    print(""" 
    """)
    print("1. Responde las preguntas correctamente para ganar puntos.")
    print("2. Cada respuesta correcta te da un punto.")
    print("3. El jugador tiene un 3 intentos para responder correctamente a cada pregunta.")
    print("4. El juego termina cuando llegas a 5 puntos o respondes 3 preguntas incorrectamente.")
    print("5. ¡Diviértete y aprende sobre las mujeres en la música!")
    print(""" 
    """)
    print(""" 
    """)
    input("Presiona Enter para comenzar...")
mostrar_mensaje_bienvenida()
#si quiero ir guardando las preguntas que ya se han hecho, puedo usar un set para almacenar las preguntas ya realizadas
preguntas_realizadas = set()   #para ir guardando las preg en un set

def seleccionar_pregunta(preguntas):
    pregunta = random.choice(list(preguntas.keys()))        #seleccionar preg aleatoria
    while pregunta in preguntas_realizadas:                 #mientras la preg este en el set de preg realizadas, seguir seleccionando preg
        pregunta = random.choice(list(preguntas.keys()))
    preguntas_realizadas.add(pregunta)                      #agrego la preg al set
    respuesta = preguntas[pregunta]                         #guardo la resp correcta en respuesta
    return pregunta, respuesta                              #devuelvo preg y resp

#Funciones para festejo de correcto o incorrecto

#Funcion para imprimir confeti
def imprimir_confeti():
    for _ in range(5):
        print(" " + random.choice(['*', '+', '•', '#', '☆', '✿']) + "    " +
              random.choice(['*', '+', '•', '#', '☆', '✿']) + "    " +
              random.choice(['*', '+', '•', '#', '☆', '✿']) * 2 + "     " +
              random.choice(['*', '+', '•', '#', '☆', '✿']) + " " +
              random.choice(['*', '+', '•', '#', '☆', '✿']) * 2 + "   " +
              random.choice(['*', '+', '•', '#', '☆', '✿']) + "   " +
              random.choice(['*', '+', '•', '#', '☆', '✿']) + "   " +
              random.choice(['*', '+', '•', '#', '☆', '✿']) * 2 + "   " +
              random.choice(['*', '+', '•', '#', '☆', '✿']) + "    " +
              random.choice(['*', '+', '•', '#', '☆', '✿']) + "   " +
              random.choice(['*', '+', '•', '#', '☆', '✿']) * 2 + "   " +
              random.choice(['*', '+', '•', '#', '☆', '✿']) + "    " +
              random.choice(['*', '+', '•', '#', '☆', '✿']) + "   " +
              random.choice(['*', '+', '•', '#', '☆', '✿']) * 2 + "   " +
              random.choice(['*', '+', '•', '#', '☆', '✿']))
        time.sleep(0.1)

#Funcion para imprimir lluvia
def imprimir_lluvia():
    for _ in range(5):
        print(" " + random.choice(['.', "'", '`', '·', ':']) * random.randint(1, 2) + "    " +
              random.choice(['.', "'", '`', '·', ':']) + "    " +
              random.choice(['.', "'", '`', '·', ':']) * 2 + "     " +
              random.choice(['.', "'", '`', '·', ':']) + " " +
              random.choice(['.', "'", '`', '·', ':']) * 2 + "   " +
              random.choice(['.', "'", '`', '·', ':']) + "   " +
              random.choice(['.', "'", '`', '·', ':']) + "   " +
              random.choice(['.', "'", '`', '·', ':']) * 2 + "   " +
              random.choice(['.', "'", '`', '·', ':']) + "    " +
              random.choice(['.', "'", '`', '·', ':']) + "   " +
              random.choice(['.', "'", '`', '·', ':']) * 2 + "   " +
              random.choice(['.', "'", '`', '·', ':']) + "    " +
              random.choice(['.', "'", '`', '·', ':']) + "    " +
              random.choice(['.', "'", '`', '·', ':']) + "   " +
              random.choice(['.', "'", '`', '·', ':']) * 2 + "   " +
              random.choice(['.', "'", '`', '·', ':']) + "   " +
              random.choice(['.', "'", '`', '·', ':']) * 2 + "   " +
              random.choice(['.', "'", '`', '·', ':']))
        time.sleep(0.1)

#Funcion para imprimir mensaje de respuesta correcta 
def imprimir_correcto():
    imprimir_confeti()
    print("\033[92m") 
    print("""
 ██████  ██████  ██████  ██████  ███████  ██████ ████████  ██████  ██ 
██      ██    ██ ██   ██ ██   ██ ██      ██         ██    ██    ██ ██ 
██      ██    ██ ██████  ██████  █████   ██         ██    ██    ██ ██ 
██      ██    ██ ██   ██ ██   ██ ██      ██         ██    ██    ██    
 ██████  ██████  ██   ██ ██   ██ ███████  ██████    ██     ██████  ██ 
""")
    print("\033[0m")  # Resetear color
    imprimir_confeti()

#Funcion para imprimir mensaje de respuesta correcta
def imprimir_incorrecto():
    imprimir_lluvia()
    print("\033[91m")  # Cambiar a color rojo
    print("""
██ ███    ██  ██████  ██████  ██████  ██████  ███████  ██████ ████████  ██████  
██ ████   ██ ██      ██    ██ ██   ██ ██   ██ ██      ██         ██    ██    ██ 
██ ██ ██  ██ ██      ██    ██ ██████  ██████  █████   ██         ██    ██    ██ 
██ ██  ██ ██ ██      ██    ██ ██   ██ ██   ██ ██      ██         ██    ██    ██ 
██ ██   ████  ██████  ██████  ██   ██ ██   ██ ███████  ██████    ██     ██████   
""")
    print("\033[0m")  # Resetear color
    imprimir_lluvia()
#3. Utiliza un bucle `while` para hacer preguntas hasta que el jugador responda un número específico de preguntas correctamente
#  o alcance un número máximo de respuestas incorrectas.


def jugar_dificil():
    print("¡Comencemos el juego \n")
    print("\033[93m")
    print("""
    ███    ██ ██ ██    ██ ███████ ██          ██████  ██ ███████ ██  ██████ ██ ██      
    ████   ██ ██ ██    ██ ██      ██          ██   ██ ██ ██      ██ ██      ██ ██      
    ██ ██  ██ ██ ██    ██ █████   ██          ██   ██ ██ █████   ██ ██      ██ ██      
    ██  ██ ██ ██  ██  ██  ██      ██          ██   ██ ██ ██      ██ ██      ██ ██      
    ██   ████ ██   ████   ███████ ███████     ██████  ██ ██      ██  ██████ ██ ███████ 
    """)                                                                            
    print("\033[0m")                                                                                   
    print("¡Vas a por todas! ¡Sorpréndeme!")
    print("Recuerda que tienes 3 intentos para responder cada pregunta.")
    print("Responde correctamente a 5 preguntas para ganar o responde incorrectamente a 3 preguntas para perder.")
    print("¡Buena suerte!")
    correctas = 0
    incorrectas = 0 
    while correctas < 5 or incorrectas == 3:
        intentos = 0
        if incorrectas == 3:
            print("\n¡Lo siento!. Has alcanzado el número máximo de respuestas incorrectas. Fin del juego.")
            imprimir_lluvia()
            print("\033[35m") 
            print("""
██ ███    ██ ████████ ███████ ███    ██ ████████  █████  ██       ██████      ██████  ███████     ███    ██ ██    ██ ███████ ██    ██  ██████  
██ ████   ██    ██    ██      ████   ██    ██    ██   ██ ██      ██    ██     ██   ██ ██          ████   ██ ██    ██ ██      ██    ██ ██    ██ 
██ ██ ██  ██    ██    █████   ██ ██  ██    ██    ███████ ██      ██    ██     ██   ██ █████       ██ ██  ██ ██    ██ █████   ██    ██ ██    ██ 
██ ██  ██ ██    ██    ██      ██  ██ ██    ██    ██   ██ ██      ██    ██     ██   ██ ██          ██  ██ ██ ██    ██ ██       ██  ██  ██    ██ 
██ ██   ████    ██    ███████ ██   ████    ██    ██   ██ ███████  ██████      ██████  ███████     ██   ████  ██████  ███████   ████    ██████                                                                                                                                
                 """)                                                                                    
            print("\033[0m")  
            imprimir_lluvia()
            break
        pregunta, respuesta = seleccionar_pregunta(preguntas_respuestas_dificil)
        print("\033[1m")  # Cambiar a negrita
        print(pregunta)
        print("\033[0m")  # Resetear estilo
        respuesta_usuario = input("Tu respuesta: ")
        if respuesta_usuario.lower() == "salir":
            print("\nGracias por jugar. ¡Nos vemos a la próxima!")
            break
        if respuesta_usuario.lower() == respuesta.lower():
            imprimir_correcto()
            correctas += 1
        else:
            #intentos += 1
            while intentos < 2 and respuesta_usuario.lower() != respuesta.lower():
                print("\033[35m")
                print("\nRespuesta incorrecta. Intenta de nuevo.")
                print("\033[0m")
                respuesta_usuario = input("Tu respuesta: ")
                intentos += 1
            incorrectas += 1
            imprimir_incorrecto()
            print(f"\nLa respuesta correcta es:{respuesta}")
            if respuesta_usuario.lower() == "salir":
                print("\nGracias por jugar. ¡Nos vemos a la próxima!")
                break
            
        print(f"\nRespuestas correctas: {correctas}, Respuestas incorrectas: {incorrectas}")
        if correctas == 5:
            print("\n¡Ganaste el juego!")
            imprimir_confeti()
            print("\033[32m") 
            print("""
                    ███████ ███████ ██      ██  ██████ ██ ████████  █████   ██████ ██  ██████  ███    ██ ███████ ███████ 
                    ██      ██      ██      ██ ██      ██    ██    ██   ██ ██      ██ ██    ██ ████   ██ ██      ██      
                    █████   █████   ██      ██ ██      ██    ██    ███████ ██      ██ ██    ██ ██ ██  ██ █████   ███████ 
                    ██      ██      ██      ██ ██      ██    ██    ██   ██ ██      ██ ██    ██ ██  ██ ██ ██           ██ 
                    ██      ███████ ███████ ██  ██████ ██    ██    ██   ██  ██████ ██  ██████  ██   ████ ███████ ███████ 
                 """)                                                                                    
            print("\033[0m")  
            imprimir_confeti()                                                                                        
        



def jugar_facil():
    print("¡Comencemos el juego \n")
    print("\033[95m")
    print("""
    ███    ██ ██ ██    ██ ███████ ██          ███████  █████   ██████ ██ ██      
    ████   ██ ██ ██    ██ ██      ██          ██      ██   ██ ██      ██ ██      
    ██ ██  ██ ██ ██    ██ █████   ██          █████   ███████ ██      ██ ██      
    ██  ██ ██ ██  ██  ██  ██      ██          ██      ██   ██ ██      ██ ██      
    ██   ████ ██   ████   ███████ ███████     ██      ██   ██  ██████ ██ ███████ 
    """)                                                                            
    print("\033[0m") 
    print("Recuerda que tienes 3 intentos para responder cada pregunta.")
    print("Responde correctamente a 5 preguntas para ganar o responde incorrectamente a 3 preguntas para perder.")
    print("¡Buena suerte!")
    correctas = 0
    incorrectas = 0 
    while correctas < 5 or incorrectas == 3:
        intentos = 0
        if incorrectas == 3:
            print("¡\nLo siento!. Has alcanzado el número máximo de respuestas incorrectas. Fin del juego.")
            imprimir_lluvia()
            print("\033[35m") 
            print("""
██ ███    ██ ████████ ███████ ███    ██ ████████  █████  ██       ██████      ██████  ███████     ███    ██ ██    ██ ███████ ██    ██  ██████  
██ ████   ██    ██    ██      ████   ██    ██    ██   ██ ██      ██    ██     ██   ██ ██          ████   ██ ██    ██ ██      ██    ██ ██    ██ 
██ ██ ██  ██    ██    █████   ██ ██  ██    ██    ███████ ██      ██    ██     ██   ██ █████       ██ ██  ██ ██    ██ █████   ██    ██ ██    ██ 
██ ██  ██ ██    ██    ██      ██  ██ ██    ██    ██   ██ ██      ██    ██     ██   ██ ██          ██  ██ ██ ██    ██ ██       ██  ██  ██    ██ 
██ ██   ████    ██    ███████ ██   ████    ██    ██   ██ ███████  ██████      ██████  ███████     ██   ████  ██████  ███████   ████    ██████                                                                                                                                
                 """)                                                                                    
            print("\033[0m")  
            imprimir_lluvia()
            break
        pregunta, respuesta = seleccionar_pregunta(preguntas_opciones_facil)
        print("\033[1m")  # Cambiar a negrita
        print(pregunta)
        print("\033[0m")  # Resetear estilo
        respuesta_usuario = input("Tu respuesta: ")
        if respuesta_usuario.lower() == "salir":
            print("Gracias por jugar. ¡Nos vemos a la próxima!")
            break
        if respuesta_usuario.lower() == respuesta.lower():
            imprimir_correcto()
            correctas += 1
        else:
            #intentos += 1
            while intentos < 2 and respuesta_usuario.lower() != respuesta.lower():
                print("\033[35m")
                print("\nRespuesta incorrecta. Intenta de nuevo.")
                print("\033[0m")
                respuesta_usuario = input("Tu respuesta: ")
                intentos += 1
            incorrectas += 1
            imprimir_incorrecto()
            print(f"La respuesta correcta es:{respuesta}")
            if respuesta_usuario.lower() == "salir":
                print("Gracias por jugar. ¡Nos vemos a la próxima!")
                break
            
        print(f"Respuestas correctas: {correctas}, Respuestas incorrectas: {incorrectas}")
        if correctas == 5:
            print("\n¡Ganaste el juego!")
            imprimir_confeti()
            print("\033[32m") 
            print("""
                    ███████ ███████ ██      ██  ██████ ██ ████████  █████   ██████ ██  ██████  ███    ██ ███████ ███████ 
                    ██      ██      ██      ██ ██      ██    ██    ██   ██ ██      ██ ██    ██ ████   ██ ██      ██      
                    █████   █████   ██      ██ ██      ██    ██    ███████ ██      ██ ██    ██ ██ ██  ██ █████   ███████ 
                    ██      ██      ██      ██ ██      ██    ██    ██   ██ ██      ██ ██    ██ ██  ██ ██ ██           ██ 
                    ██      ███████ ███████ ██  ██████ ██    ██    ██   ██  ██████ ██  ██████  ██   ████ ███████ ███████ 
                 """)                                                                                    
            print("\033[0m")  
            imprimir_confeti()                        
        

def nivel_juego():
    nivel = input("Seleccione el nivel de dificultad (1 o 2)\n"
                "1. Fácil: se muestran diferentes opciones posibles\n"
                "2. Difícil: se responde con la respuesta correcta directamente\n"
                "Escriba 'salir' para terminar el juego: ").lower()
    if nivel == "1":
        jugar_facil()           #aca no se si deberiamos llamar a la funcion especifica o tener una funcion en la que se elija el nivel dentro
    elif nivel == "2":
        jugar_dificil()
    elif nivel == "salir":
        print("¡Qué lástima que no te atrevas! Hasta la próxima.")
    else:
        print("Opción no válida. Por favor, elige 1 o 2.")
def jugar():
    mostrar_mensaje_bienvenida()
    nivel_juego()
    
jugar()