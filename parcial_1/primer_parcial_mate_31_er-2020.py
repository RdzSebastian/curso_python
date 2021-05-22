#Alumno = Nicolas Burgueño

from matplotlib import pyplot as plt
from matplotlib_venn import venn3,venn3_circles

#Funciones

def sumadic(**dic):            #Suma el diccionario
    z=0
    for i in auto.values():
        z+=i
    return z

def suma(*args):               #Para sumar la lista y la tupla
    s=0
    for i in args:
        s+=i
    return s

resta = lambda u,v,x,y:u-v-x-y #Calcula el total de uno de los circulos del diagrama de venn
suma_v = lambda u,v,x:u+v+x    #Calcula el total de personas con un vehiculo 

#Variables

moto = [14, 17, 9, 13, 15, 12]
bici = (17, 8, 9, 7, 10, 11, 12, 4, 12)
auto = {"Chico":27,"Mediano":17,"Grande":16}

moto = suma(*moto)              #total de motos
bici = suma(*bici)              #total de bicis
auto = sumadic(**auto)          #total de autos
ningun = 2                      #ningun vehiculo
tres_v = 55                     #tres vehiculos
ba = 2                          #bici y auto
mb = 18                         #moto y bici
soloa = 1                       #solo auto

#Respuestas

solob = resta(bici ,tres_v ,mb ,ba ) #Porcentaje de los que tienen bici                (respuesta 4)
ma = resta(auto ,tres_v ,ba ,soloa ) #Porcentaje de los que tienen moto y auto         (respuesta 2)
solom = resta(moto ,tres_v ,mb ,ma ) #Porcentaje de los que tienen solo moto      (respuesta 3)
un_vec = suma_v (solob ,solom ,soloa ) #Porcentaje de los que tienen un vehiculo     (respuesta 1)

#Diagrama de venn

diagrama = venn3((1,1,1,1,1,1,1),set_labels=("Moto","Bicicleta","Auto"),alpha=0.8)

#Etiquetas de las partes

diagrama.get_label_by_id('100').set_text(solom)
diagrama.get_label_by_id('010').set_text(solob)
diagrama.get_label_by_id('001').set_text(soloa)
diagrama.get_label_by_id('110').set_text(mb)
diagrama.get_label_by_id('101').set_text(ma)
diagrama.get_label_by_id('011').set_text(ba)
diagrama.get_label_by_id('111').set_text(tres_v)

venn3_circles(subsets=(1,1,1,1,1,1,1),color="#000000",alpha=1,linestyle="-",linewidth="3")

plt.title("Sin vehiculo = 2%")
plt.show()


