suppi_temp = int(input("Sisesta supi algtemperatuur: "))
ruumi_temp = int(input("Sisesta ruumi temperatuur: "))

while suppi_temp - 0.01 > ruumi_temp:
    print("Supi temperatuur on", suppi_temp)
    vahe = suppi_temp - ruumi_temp
    suppi_temp -= vahe * 0.19