# Faça um programa que receba um número em segundos,
# converta esse número para horas, minuto e segundos.
# Exemplos:

# Entrada: 556
# Saída: 0:9:16

# Entrada: 140153
# Saída: 38:55:53

segundos = int(input("Entre com um número em segundos: "))

horas = segundos // (60*60) # horas inteiras

segundos = segundos % (60*60) # resto de segundos da divisao por hora

minutos = segundos // 60 # minutos inteiros

segundos = segundos % 60 # resto de segundos da divisão por minuto

print(horas, minutos, segundos, sep=":")