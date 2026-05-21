clientes= [
    [1,350,15],
    [2,220,10],
    [3,100,8],
    [4,40,25],
    [5,55,20]

]

def nivel_compromiso(duracion, clics):
    if duracion >= 200 and clics >= 10:
        return "ALTO"
    elif duracion < 60 or clics < 3:
        return "BAJO"
    else:
        return "MEDIO"
    

for cliente in clientes:
    id_cliente= cliente[0]
    duracion= cliente[1]
    clics= cliente[2]
    nivel=nivel_compromiso(duracion,clics)
    print(f"cliente: {id_cliente}, {duracion} segundos,{clics} clics, nivel de compromiso: {nivel}")
