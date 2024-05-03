1. Para promocionar un nuevo producto una empresa desea contratar influencers para la difusión del mismo. Para cada uno de ellos han calculado un “valor de penetración de mercado”.
Cuanto mayor este valor, mayor posibilidad de que mas de sus seguidores se interesen en el producto. Este valor corresponde a un número entero positivo. 
Existen pares de influencers que por diversos motivos no quieren o no pueden trabajar juntos. Esta información es conocida por la empresa.

Nos solicitan que determinemos a que influencers contratar para maximizar el valor de penetración de mercado (los valores de los influencers contratados se suman para establecer el total.
Se pide:

 - Proponga y explique una solución del problema mediante Branch and Bound.

 - Brinde un ejemplo simple paso a paso del funcionamiento de su solución.

 - Programe su propuestaa

Formato de los archivos:
El programa debe recibir por parámetro un archivo con los influencers. Ejemplo:

python promocion.py influencers.txtt

2. Una compañia agrícola debe determinar la separación en regiones de campos de n*n hectómetros (si, solo de este tamaño y además cuando “n” es un número entero potencia de 2 y mayor o igual a 2).
Cada región debe tener forma en L (como se muestra en celeste en la figura). Se puede ver la region como conformada por 3 cuadrados cada uno de 1x1 (1 hectarea).
Dentro del campo existe una hectarea donde se ubican los silos de almacenamiento y no se puede cultivar (Se muestra en la figura de ejemplo como un cuadrado negro).

Nos piden que, dado un campo con un valor “n” y una ubicación de los silos en una posición x,y (medido desde la punta superior izquierda), determinemos como separarlo en regiones.

Se pide:
 - Presentar un algoritmo que lo resuelva utilizando división y conquista.

 - Brindar un ejemplo de funcionamiento

 - Programe su solución

Formato de los archivos:
El programa debe recibir por parámetro el tamaño n del campos y la posición de los silos. Ejemplo:

python regionalizar.py 4 2 1
Corresponde a un campo de 4x4 donde los silos se encuentran en la hectarea (2,1).

Debe resolver el problema y retornar por pantalla la regionalización de forma que se puede entender visualmente.
