Los equipos son de 5 contra 5.<br>
Parte atacando el héroe del equipo A, luego del equipo B y así sucesivamente.<br>
Como especifica el enunciado, si un héroe derrota a su rival, se recupera la vida del ganador, y éste pasa a la siguiente ronda contra un nuevo rival.<br>
Todo lo demás sigue el enunciado.

Consideraciones:
  - Para correr la simulación se ejecuta main.py con python 3.
  - Deben tener los archivos main, clases y data en la misma carpeta. La api key de mailgun en el archivo data.py debe ser reemplazada, pues mailgun no permite que suba la key a un repositorio público (desactivó mi api key).
  - Frecuentemente los superhéroes derrotan a su rival de un solo golpe (esperable al poner a Paul Blart: mall cop vs Thanos)
  - Muy rara vez, pero ocurre, pelearán dos superhéroes muy débiles, apenas inflingiéndose daño, por lo que conviene detener la simulación en esos casos. Pues puede demorarse mucho en terminar.
  - Hay superhéroes con alignment 'neutral', a ellos no se les aplica el buff o debuff de equipo
  - El BONUS del mail está correctamente implementado. Pueden probarlo.
