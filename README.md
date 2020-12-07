# genero y lenguajes
Análisis de correlación entre sexo del desarrollador y sus lenguajes de computación.

# Metodología
Los datos son tomados de una encuesta anual realizada por stackoverflow. Información sobre esta y su metodología se pueden encontrar en https://insights.stackoverflow.com/survey/2020

# Sesgos
Stackoverflow es un recurso de aprendizaje principalmente inglés. Sus usuarios son o hablantes nativos, o consideran el inglés como lingua franca, por ello lenguajes como Python estaran sobrepesados comparado con lenguajes más simbolicos como Perl o Haskell.
Stackoverflow tambien es un recurso abierto tipo wiki, por lo que lenguajes y plataformas para la construcción de sistemas abiertos estaran sobrepesados. 

La elección de lenguajes está limitada y definida de antemano, lo cual limita las respuestas, se puede notar una tendencia hacia lenguajes modernos, sin lenguajes previos a 1980. Estos son: 
{'JavaScript', 'Java', 'Perl', 'Julia', 'Kotlin', 'Scala', 'HTML/CSS', 'NA', 'Dart', 'Assembly', 'Python', 'R', 'Swift', 'Go', 'Haskell', 'PHP', 'Ruby', 'SQL', 'TypeScript', 'Bash/Shell/PowerShell', 'Objective-C', 'Rust', 'C', 'VBA', 'C#', 'C++'}
Esta limitación es particularmente importante para la correlación entre genero y lenguajes ya que la proporción de programadoras mujeres a hombres solía ser más pareja previo a 1980.

# Resultados preliminares

Aproximadamente el 8% de los programadores que respondieron a la encuesta de StackOverflow son mujeres [1] . Aproximadamente el 12% de los usuarios de R son mujeres. [2]


[1] https://insights.stackoverflow.com/survey/2020#developer-profile-gender-all-respondents2
Vease el codigo para a.py en este repo. 
