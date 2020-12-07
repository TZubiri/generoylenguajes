f = open("./survey_results_public.csv")
c = f.read()
# len(c) ~== os.stat("./survey_results_public.csv").st_size
lineseps = [i for i,x in enumerate(c) if x == '\n']
# len(lines) == 64462
# lines[0] == 799
header = c[0:lineseps[0]]
columns = header.split(',')
columns2 = {v:i for i,v in enumerate(columns)}
#columns2['gender'] == 17

# c[lines[1]:lines[2]].split(',')[columns2['gender']] == 'B.S' # ???
# c[lines[3]:lines[4]].split(',')[columns2['Age']] == '25'  # Bien

# c[lines[1]:lines[2]] ~== 'blabla,blabla,blabla,"bla,bla,B.S,bla",bla'

def comas(line):
  i = 0
  encomillas = False
  seps = [] # comas separadoras
  while i<len(line):
    c = line[i]
    if c == '\\':
      #previniendo problemas con \ como caracter de escape para comillas y comas.
      i+=2 # ignoro el siguiente caracter.
      #Puede haber problemas si el \ escapaba un newline, pero espero que no pase.
      continue
    elif c == '"' :
      encomillas = not encomillas
      i+=1
      continue
    elif c == "," and encomillas == False :
      seps.append(i)
      i+=1
      continue
    i=i+1
  return seps

l4 = c[lineseps[4]:lineseps[5]]
s4 = comas(l4)
# g4 = l4[ s4[columns2["Gender"]-1] : s4[columns2["Gender"]] ]
# g4 == ",Man"
# g4[1:] == "Man"

#lang4 = l4[ s4[columns2["LanguageWorkedWith"]-1] : s4[columns2["LanguageWorkedWith"]] ]

#langs4 = lang4.split(';')

#Predicciones: R tendra una proporcion mas femenina que lo comun, porque las estadisticas son de mayor interes que la programacion. R tendra una proporcion mas femenina que Python y este tendra una razón mas femenina que C
#Cobol y fortran tendran una proporcion mas femenina debido a su edad, la proporcion de desarrolladores era mas pareja previo a los 85. Lamentablemente estos lenguajes no se incluyen en el dataset de stackoverflow
# C# tendra una proporcion ligeramente mas femenina debido a que a las mujeres no les atrae el movimiento de software libre.
# CSS tendra una proporcion notablemente mas femenina debido a que se usa para definir cuestiones esteticas, para diseñar y brindar color a las aplicaciones.
# Lamentablemente HTML y CSS estan juntos en la encuesta.
#Finalmente lenguajes como SQL y VBA son incluidos para corroborar si tienen una razón más femenina, ya que son lenguajes intricamente relacionados con la estadistica a grande y mediana escala respectivamente.

lenguajes_medidos = ['R','Python','C','C#','HTML/CSS','JavaScript','SQL','VBA']

upg = {} #usuarios por genero
for l in lenguajes_medidos:
  upg[l] = {'m':0,'w':0,'o':0}


lenguajes_totales = set()
for i in range(len(lineseps)-1):
  de = lineseps[i]
  a = lineseps[i+1]
  line = c[de:a]
  s = comas(line)
  gc = columns2["Gender"]
  g = line[ s[gc-1] : s[gc] ]
  g = g[1:] #borro coma principal
  lc = colu
