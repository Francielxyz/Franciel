# Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho
# em metros quadrados da área a ser pintada. Considere que a cobertura da tinta
# é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de
# 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
# Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços
# em 3 situações:
# comprar apenas latas de 18 litros;
# comprar apenas galões de 3,6 litros;
# misturar latas e galões, de forma que o preço seja o menor. Acrescente 10% de
# folga e sempre arredonde os valores para cima, isto é, considere latas cheias.
import math
escolha=int(input("""Para comprar litros de tintas digite (1):
Rara comprar galões digite (2):
Para misturar litros de tintas com galões digite (3):
"""))
if(escolha==1):
    metros=int(input("Quantos metros quadrados é a área a ser pintada? "))
    x = metros / 6
    y = x / 18
    y = math.ceil(y)
    print("Você precisará de",y,"latas de tintas")
    print("O valor a ser pago é de:", y*80,"R$")
elif (escolha==2): # galões de 3,6 litros, que custam R$ 25,00. 1 litro pnta 6 metros quadrado
    metros=int(input("Quantos metros quadrados é a área a ser pintada? "))
    x=metros/6
    y=x/3.6
    y= math.ceil(y)
    print("Você vai precisar de",y,"galões de tintas")
    print("O valor a ser pago vai é de", y*25,"R$")
elif (escolha==3): #mistura de latas de tintas com galões de tintas
    metros=int(input("Quantos metros quadrados é a área a ser pintada? "))
    a=metros/6
    b=(metros%18)
    litros=a/18
    galoes=b/3.6
    litros= math.floor(litros)
    galoes= math.ceil(galoes)
    if(litros==0 and galoes==1):
        print("Voce vai usar", galoes,"galão de tinta e não necessita comprar latas tintas")
        print("Valor a ser pago é de", galoes*25,"R$")
    elif(litros==0 and galoes>=2):
        print("Você vai usar", galoes,"galões de tintas e não precisa comprar latas de tintas")
        print("Valor a ser pago é de", galoes*25,"R$")
    elif(litros==1 and galoes==0):
        print("Você vai usar",litros,"lata de tinta e não precisa comprar galões de tinta")
        print("Valor a ser pago é de", litros*80,"R$")
    elif(litros==1 and galoes==1):
            print("Você vai usar", litros,"litro de tintas e", galoes,"galão de tinta")
            print("Valor a ser pago é de",litros*80,"R$ em litros de tintas e", galoes*25,"R$ em galão de tintas")
            print("Totalizando", litros*80 + galoes*25,"R$")
    elif(litros==1 and galoes>=2):
            print("Você vai usar", litros,"litro de tintas e", galoes,"galões de tintas")
            print("Valor a ser pago é de",litros*80,"R$ em litros de tintas e", galoes*25,"R$ em galão de tintas")
            print("Totalizando", litros*80 + galoes*25,"R$")
    elif(litros>=2 and galoes>=2):
            print("Você vai usar", litros,"litros de tintas e", galoes,"galões de tintas")
            print("Valor a ser pago é de",litros*80,"R$ em litros de tintas e", galoes*25,"R$ em galão de tintas")
            print("Totalizando", litros*80 + galoes*25,"R$")
