import wave
import numpy as np
import matplotlib.pyplot as plt

#carcar archivo wav en la variable
good_morning = wave.open('good-morningMan.wav', 'r')

#obtener todos los fromas del objeto wave
frames = good_morning.readframes(-1)

#mostrar el resultado de frames
#print(signal_gm[:10])
#print(signal_gm)

#Convierte el audio good morning de bytes a enteros
ondaconvertida = np.frombuffer(frames, dtype='int16')

#Imprime los 10 primeros valores de la onda.
#print(ondaconvertida[:10])

framerate_gm = good_morning.getframerate()

print(framerate_gm)

time_gm = np.linspace(start=0, stop=len(ondaconvertida)/framerate_gm, num=len(ondaconvertida))
print(time_gm[:10])


#lo mismo de arriba pero en good afternoon
good_afternoon = wave.open('good-afternoon.wav', 'r')

framesafter = good_afternoon.readframes(-1)

ondaconvertidaafter = np.frombuffer(framesafter, dtype='int16')

framerate_ga = good_afternoon.getframerate()

print(framerate_ga)

time_ga = np.linspace(start=0, stop=len(ondaconvertidaafter)/framerate_ga, num=len(ondaconvertidaafter))
print(time_ga[:10])

#Siguientes pasos
#generacion de la grafica
plt.title('good morning vs Good afternoon')

#etiquetas de los ejes
plt.xlabel('Tiempo (segundos)')
plt.ylabel('Amplitud')

#agregar informacion de las ondas para graficar
plt.plot(time_ga, ondaconvertidaafter, label="good afternoon")
plt.plot(time_gm, ondaconvertida, label="Good Morning", alpha=0.5)

plt.legend()
plt.show()