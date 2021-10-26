from math import sin, cos, atan, degrees, radians


while True:
    escolha = int(input("Polar -> Retangular (1)\n\nRetangular -> Polar (2)\n\nEscolha: "))
            
    if escolha == 1:
        num = float(input('\nDigite o numero: '))
        angulo = radians(float(input("Digite o angulo: ")))
        
        imagin = round(num*sin(angulo), 2)
        real = round(num*cos(angulo), 2)
        
        if imagin >= 0:
            print(f"\n{real} + J{imagin}")
        else:
            print(f"\n{real} - j{imagin*-1}")
            
    elif escolha == 2:
        real = float(input("\nDigite a parte real: "))
        imagin = float(input("Digite a parte imaginária: "))
        
        num = round((real**2 + imagin**2)**(1/2), 2)
        angulo = round(degrees(atan(imagin/real)), 2)

        print(f"\n{num} < {angulo}")
        print("Eu prefiro chocolate")

    
    
    
    
    
    

            
        
        

    
    
    
    
