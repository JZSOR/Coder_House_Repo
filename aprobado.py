import sys

def ayuda():
    print('''
          Tienes que ingresar las calificaciones de dos parciales 
          Estos se van a promediar y diran si paso la materia
          Escribirlos de la siguiente manera:
          python aprobado.py {Calificacion 1} {Calificacion 2}
          ''')

if len(sys.argv) < 3:
    ayuda()
    exit()

try:
    cal_1 = float(sys.argv[1])
    cal_2 = float(sys.argv[2])
except ValueError:
    print('Deben de ser valores numericos')
    exit()
    
if cal_1 > 10 or cal_2 > 10:
    print('Deben de ser numeros entre 0 y 10')
    print(f'Primer parcial: {cal_1}')
    print(f'Segundo parcial: {cal_2}')

elif cal_1 < 0 or cal_2 < 0:
    print('Deben de ser numeros entre 0 y 10')
    print(f'Primer parcial: {cal_1}')
    print(f'Segundo parcial: {cal_2}')

elif cal_1 >= 7 and cal_2 >= 7:
    print('Promocionado')

elif cal_1 >= 4 and cal_2 >= 4:
    print('Aprobado, debe rendir final')

elif cal_1 < 4 and cal_2 < 4:
    print('Desaprobo ambos parciales, debe recursar')
    
elif cal_1 < 4 and cal_2 >= 4:
    print('Desaprobado, debe recuperar el primer parcial')

elif cal_1 >= 4 and cal_2 < 4:
    print('Desaprobado, debe recuperar el segundo parcial')

else:
    ayuda()