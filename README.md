# langchain

Permite utilizar o consumir multiples modelos o apis y poderlos concatenar para crear un modelo mejor. 

LLM: no matiene el contexto de la conversacion

embed: los modelos de lenguaje procesan numeros (representacion vectorial). Cuando tienen el mimso significado se encuentran cerca al mismo nivel. Para la similitud se maneja con el calculo de cosenos. 

one-hot encoding: codifica las variables para un  mejor procesamiento de los modelos de lenguaje (revisa que hay semanticamente similares)

Mecanismo de atencion: que palabras tienen mas peso para establecer una relacion 

Sampling: permite generar un texto unico mediante un numero aleatorio 


## Formas de interactuar con los documentos 
* Stuff: permite uso de documentos pequenos 
* Refind: 
* Map reduce: de una gran cantidad de informacion la filtra, realiza la comprencion de la informacion y envia la respuesta. Realizando varias peticiones al modelo.
* Map re-tank: la respuesta con el socre mayor muentra la respuesta  

## Almacen de vectores 
* Chroma: para el almacenamiento de los embedding 
* RetrievalQA: para el manejo de las preguntas hacia los documentos (se debe ejecutar con run para que tenga un contexto)



## Librerias 
```sh 
pip install langchain
pip install pypdf
pip install openAI
pip install tiktoken -- para la tokenizacion de las palabras 
pip install chromadb
```

## Notas
* los token miden la cantidad de promt a enviar 
* Al usar probailidades la respuesta no es tan exacta 
* RLHF: aprendizaje reforzado por feedback humano (del entrenamiento genera 4 respuesta y son calificadas como mejor respuestas, tras este filtro pasa al modelo de produccion)


# Front 

### Librerias 
```sh
pip install fastapi -- 
pip install "uvicorn[standard]" -- para el motor 
```