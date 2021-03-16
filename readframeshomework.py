import wave
import numpy as np
import matplotlib.pyplot as plt

#Lo mismo pero en cri-d-effroi-scream
print('Scream')

scream = wave.open('cri-d-effroi-scream.wav', 'r')

framesscream = scream.readframes(-1)

print(framesscream[:10])

ondaconvertidascream = np.frombuffer(framesscream, dtype='int16')

print(ondaconvertidascream[:10])

framerate_scrm = scream.getframerate()

print(framerate_scrm)

time_scrm = np.linspace(start=0, stop=len(ondaconvertidascream)/framerate_scrm, num=len(ondaconvertidascream))
print(time_scrm[:10])

#Lo mismo pero en Kaa
print('KaaAudio')
screamkaa = wave.open('kaa.wav', 'r')

frameskaa = screamkaa.readframes(-1)

print(frameskaa[:10])

ondaconvertidaskaa = np.frombuffer(frameskaa, dtype='int16')

print(ondaconvertidaskaa[:10])

framerate_kaa = screamkaa.getframerate()

print(framerate_kaa)

time_kaa = np.linspace(start=0, stop=len(ondaconvertidaskaa)/framerate_kaa, num=len(ondaconvertidaskaa))
print(time_kaa[:10])


#Siguientes pasos
#generacion de la grafica
plt.title('Scream vs Kaa')

#etiquetas de los ejes
plt.xlabel('Tiempo (segundos)')
plt.ylabel('Amplitud')

#agregar informacion de las ondas para graficar
plt.plot(time_scrm, ondaconvertidascream, label = 'scream')
plt.plot(time_kaa, ondaconvertidaskaa, label= 'kaa', alpha = 0.5)

plt.legend()
plt.show()
