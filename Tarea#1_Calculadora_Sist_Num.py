from math import trunc

def Bin_Dec(bin):
    num=0 
    pot=0
    bin = bin[::-1]
    #[start : end : step]
    for digit in bin:
        mult = 2**pot
        num+= int(digit)*mult
        pot+= 1
    return num

def Dec_Bin(num):
    bin=""
    t=0
    while(num!=0):
        t=num%2
        num=(int)(num/2)
        if(t==1):
            bin+="1"
        else:
            bin+="0"
    if(num==1):
        bin+="1"
    bin=bin[::-1]
    return bin

def Dec_to_Hex(num):
    hex=""
    t=0
    while(num!=0):
        t=num%16
        num=trunc(num/16)
        if(t==0):
            hex+="0"
        elif(t==1):
            hex+="1"
        elif(t==2):
            hex+="2"
        elif(t==3):
            hex+="3"
        elif(t==4):
            hex+="4"    
        elif(t==5):
            hex+="5"
        elif(t==6):
            hex+="6"
        elif(t==7):
            hex+="7"
        elif(t==8):
            hex+="8"
        elif(t==9):
            hex+="9"
        elif(t==10):
            hex+="A"
        elif(t==11):
            hex+="B"
        elif(t==12):
            hex+="C"
        elif(t==13):
            hex+="D"
        elif(t==14):
            hex+="E"
        elif(t==15):
            hex+="F"
    hex=hex[::-1]
    return hex

def Dec_to_Oct(num):
    oct=""
    t=0
    while(num!=0):
        t=num%8
        num=trunc(num/8)
        if(t==0):
            oct+="0"
        elif(t==1):
            oct+="1"
        elif(t==2):
            oct+="2"
        elif(t==3):
            oct+="3"
        elif(t==4):
            oct+="4"    
        elif(t==5):
            oct+="5"
        elif(t==6):
            oct+="6"
        elif(t==7):
            oct+="7"
    oct=oct[::-1]
    return oct

def Bin_to_Hex(bin):
    num=Bin_Dec(bin)
    return Dec_to_Hex(num)

def Bin_to_Oct(bin):
    num=Bin_Dec(bin)
    return Dec_to_Oct(num)

def Hex_Bin(hex):
    bin=""
    for digit in hex:
        if(digit=="0"):
            bin+="0000"
        elif(digit=="1"):
            bin+="0001"
        elif(digit=="2"):
            bin+="0010"
        elif(digit=="3"):
            bin+="0011"
        elif(digit=="4"):
            bin+="0100"
        elif(digit=="5"):
            bin+="0101"
        elif(digit=="6"):
            bin+="0110"
        elif(digit=="7"):
            bin+="0111"
        elif(digit=="8"):
            bin+="1000"
        elif(digit=="9"):
            bin+="1001"
        elif(digit=="A" or digit=="a"):
            bin+="1010" 
        elif(digit=="B" or digit=="b"):
            bin+="1011"
        elif(digit=="C" or digit=="c"):
            bin+="1100"
        elif(digit=="D" or digit=="d"):
            bin+="1101"
        elif(digit=="E" or digit=="e"):
            bin+="1110"
        elif(digit=="F" or digit=="f"):
            bin+="1111"
    return bin

def Hex_Dec(hex):
    num=0
    i=-1
    hex=hex[::-1]
    for digit in hex:
        if(digit=="0"):
            i+=1
            num+=0*(16**i)
        elif(digit=="1"):
            i+=1
            num+=1*(16**i)
        elif(digit=="2"):
            i+=1
            num+=2*(16**i)
        elif(digit=="3"):
            i+=1
            num+=3*(16**i)        
        elif(digit=="4"):
            i+=1
            num+=4*(16**i)
        elif(digit=="5"):
            i+=1
            num+=5*(16**i)        
        elif(digit=="6"):
            i+=1
            num+=6*(16**i)    
        elif(digit=="7"):
            i+=1
            num+=7*(16**i)    
        elif(digit=="8"):
            i+=1
            num+=8*(16**i)    
        elif(digit=="9"):
            i+=1
            num+=9*(16**i)    
        elif(digit=="A" or digit=="a"):
            i+=1
            num+=10*(16**i)    
        elif(digit=="B" or digit=="b"):
            i+=1
            num+=11*(16**i)      
        elif(digit=="C" or digit=="c"):
            i+=1
            num+=12*(16**i)      
        elif(digit=="D" or digit=="d"):
            i+=1
            num+=13*(16**i)      
        elif(digit=="E" or digit=="e"):
            i+=1
            num+=14*(16**i)  
        elif(digit=="F" or digit=="f"):
            i+=1
            num+=15*(16**i)      
    return num

def Hex_Oct(hex):
    dec=Hex_Dec(hex) 
    return Dec_to_Oct(dec) 

def Oct_Hex(oct):
    dec=Oct_Dec(oct)
    return Dec_to_Hex(dec)

def Oct_Bin(oct):
    bin=""
    flag=0
    for digit in oct:
        if(digit=="8" or digit=="9"):
            flag+=1
            break
        elif(digit=="0"):
            bin+="000"
        elif(digit=="1"):
            bin+="001"
        elif(digit=="2"):
            bin+="010" 
        elif(digit=="3"):
            bin+="011"
        elif(digit=="4"):
            bin+="100"
        elif(digit=="5"):
            bin+="101"
        elif(digit=="6"):
            bin+="110"
        elif(digit=="7"):
            bin+="111"
    if(flag==0):
        return bin
    else:
        return None

def Oct_Dec(oct):
    num=0
    i=-1
    g=0
    oct=oct[::-1]
    for digit in oct:
        if(digit=="8" or digit=="9"):
            g+=1 
            break 
        elif(digit=="0"):
            i+=1
            num+=0*(8**i)
        elif(digit=="1"):
            i+=1
            num+=1*(8**i)
        elif(digit=="2"):
            i+=1
            num+=2*(8**i)
        elif(digit=="3"):
            i+=1
            num+=3*(8**i)        
        elif(digit=="4"):
            i+=1
            num+=4*(8**i)
        elif(digit=="5"):
            i+=1
            num+=5*(8**i)        
        elif(digit=="6"):
            i+=1
            num+=6*(8**i)    
        elif(digit=="7"):
            i+=1
            num+=7*(8**i)    
    if(g==0):
        return num
    else:
        return None
    
def Dec_Bin_Float(num):
    d1=int(abs(num)) #parte entera
    d2=num-d1 #parte decimal 

    aux_result=0.0 #variable auxiliar

    bin1=Dec_Bin(d1) #Transformando parte entera a binario
    bin1+="."
    for i in range(3):
        d2*=2 #multiplicando por 2
        if(d2>=1.0):
            bin1+="1"
        else:
            bin1+="0"
        aux_result=int(d2)
        d2=d2-aux_result #Obteniendo solo parte decimal del resultado multilpicado
    return bin1

def Dec_Oct_Float(num):
    d1=int(abs(num)) #parte entera
    d2=num-d1 #parte decimal 

    aux_result=0.0

    oct1=Dec_to_Oct(d1)
    oct1+="."
    for i in range(3):
        d2*=8
        if(d2>=7.0):
            oct1+="7"
        elif(d2>=6.0):
            oct1+="6"
        elif(d2>=5.0):
            oct1+="5"
        elif(d2>=4.0):
            oct1+="4"
        elif(d2>=3.0):
            oct1+="3"
        elif(d2>=2.0):
            oct1+="2"
        elif(d2>=1.0):
            oct1+="1"
        else:
            oct1+="0"
        aux_result=int(d2)
        d2-=aux_result #Obteniendo solo parte decimal del resultado multilpicado
    return oct1

def Dec_Hex_Float(num):
    d1=int(abs(num)) #parte entera
    d2=num-d1 #parte decimal 

    aux_result=0.0

    hex=Dec_to_Hex(d1)
    hex+="."
    for i in range(3):
        d2*=16
        if(d2>=15.0):
            hex+="F"
        elif(d2>=14.0):
            hex+="E"
        elif(d2>=13.0):
            hex+="D"
        elif(d2>=12.0):
            hex+="C"
        elif(d2>=11.0):
            hex+="B"
        elif(d2>=10.0):
            hex+="A"
        elif(d2>=9.0):
            hex+="9"
        elif(d2>=8.0):
            hex+="8"
        elif(d2>=7.0):
            hex+="7"
        elif(d2>=6.0):
            hex+="6"
        elif(d2>=5.0):
            hex+="5"
        elif(d2>=4.0):
            hex+="4"
        elif(d2>=3.0):
            hex+="3"
        elif(d2>=2.0):
            hex+="2"
        elif(d2>=1.0):
            hex+="1"
        else:
            hex+="0"
        aux_result=int(d2)
        d2-=aux_result
    return hex

def Bin_Dec_Float(bin):
    lista=bin.split(".") #diviendo cadena en 2
    i=-1 #exponente
    entero=lista[0] #parte entera del binario
    decimal=lista[1] #parte decimal del binario

    dec=float(Bin_Dec(entero)) #transformando parte entera a base decimal
    for digit in decimal: #transformando parte con punto decimal
        dec+=int(digit)*(2**i) 
        i-=1
    return dec

def Bin_Oct_Float(bin):
    dec=Bin_Dec_Float(bin)
    return Dec_Oct_Float(dec)

def Bin_Hex_Float(bin):
    dec=Bin_Dec_Float(bin)
    return Dec_Hex_Float(dec)

def Hex_Dec_Float(hex):
    lista=hex.split(".") #diviendo cadena en 2
    i=-1 #exponente
    entero=lista[0] #parte entera del hexadecimal
    decimal=lista[1] #parte decimal del hexadecimal

    dec=float(Hex_Dec(entero)) #parte entera a decimal
    for digit in decimal:
        if(digit=="0"):
            dec+=0*(16**i)
        elif(digit=="1"): 
            dec+=1*(16**i)
        elif(digit=="2"):
            dec+=2*(16**i)
        elif(digit=="3"):
            dec+=3*(16**i)        
        elif(digit=="4"):
            dec+=4*(16**i)
        elif(digit=="5"):
            dec+=5*(16**i)        
        elif(digit=="6"):
            dec+=6*(16**i)    
        elif(digit=="7"):
            dec+=7*(16**i)    
        elif(digit=="8"):
            dec+=8*(16**i)    
        elif(digit=="9"):
            dec+=9*(16**i)    
        elif(digit=="A" or digit=="a"):
            dec+=10*(16**i)    
        elif(digit=="B" or digit=="b"):
            dec+=11*(16**i)      
        elif(digit=="C" or digit=="c"):
            dec+=12*(16**i)      
        elif(digit=="D" or digit=="d"):
            dec+=13*(16**i)      
        elif(digit=="E" or digit=="e"):
            dec+=14*(16**i)  
        elif(digit=="F" or digit=="f"):
            dec+=15*(16**i)
        i-=1
    return dec

def Hex_Bin_Float(hex):
    bin=""
    for digit in hex:
        if(digit=="."):
            bin+="."
        elif(digit=="0"):
            bin+="0000"
        elif(digit=="1"):
            bin+="0001"
        elif(digit=="2"):
            bin+="0010"
        elif(digit=="3"):
            bin+="0011"
        elif(digit=="4"):
            bin+="0100"
        elif(digit=="5"):
            bin+="0101"
        elif(digit=="6"):
            bin+="0110"
        elif(digit=="7"):
            bin+="0111"
        elif(digit=="8"):
            bin+="1000"
        elif(digit=="9"):
            bin+="1001"
        elif(digit=="A" or digit=="a"):
            bin+="1010" 
        elif(digit=="B" or digit=="b"):
            bin+="1011"
        elif(digit=="C" or digit=="c"):
            bin+="1100"
        elif(digit=="D" or digit=="d"):
            bin+="1101"
        elif(digit=="E" or digit=="e"):
            bin+="1110"
        elif(digit=="F" or digit=="f"):
            bin+="1111"
    return bin

def Hex_Oct_Float(hex):
    dec=Hex_Dec_Float(hex)
    return Dec_Oct_Float(dec)

def Oct_Dec_Float(oct):
    lista=oct.split(".") #diviendo cadena en 2
    i=-1 #exponente
    entero=lista[0] #parte entera del octal
    decimal=lista[1] #parte decimal del octal

    dec=float(Oct_Dec(entero)) #parte entera a decimal
    for digit in decimal:
        if(digit=="0"):
            dec+=0*(8**i)
        elif(digit=="1"): 
            dec+=1*(8**i)
        elif(digit=="2"):
            dec+=2*(8**i)
        elif(digit=="3"):
            dec+=3*(8**i)        
        elif(digit=="4"):
            dec+=4*(8**i)
        elif(digit=="5"):
            dec+=5*(8**i)        
        elif(digit=="6"):
            dec+=6*(8**i)    
        elif(digit=="7"):
            dec+=7*(8**i)    
        i-=1
    return dec

def Oct_Bin_Float(oct):
    bin=""
    for digit in oct:
        if(digit=="."):
            bin+="."
        elif(digit=="0"):
            bin+="000"
        elif(digit=="1"):
            bin+="001"
        elif(digit=="2"):
            bin+="010"
        elif(digit=="3"):
            bin+="011"
        elif(digit=="4"):
            bin+="100"
        elif(digit=="5"):
            bin+="101"
        elif(digit=="6"):
            bin+="110"
        elif(digit=="7"):
            bin+="111"
    return bin

def Oct_Hex_Float(oct):
    dec=Oct_Dec_Float(oct)
    return Dec_Hex_Float(dec)

def menu():
    print("\n***CALCULADORA DE CONVERSIONES A DIFERENTES BASES***")
    print("1.Binario a Decimal.")
    print("2.Binario a Hexadecimal.")
    print("3.Binario a Octal.")
    print("4.Decimal a Binario.")
    print("5.Decimal a Hexadecimal.")
    print("6.Decimal a Octal.")
    print("7.Hexadecimal a Binario.")
    print("8.Hexadecimal a Decimal.")
    print("9.Hexadecimal a Octal.")
    print("10.Octal a Hexadecimal.")
    print("11.Octal a Binario.")
    print("12.Octal a Decimal.")

cont=1
while(cont!=0):
    menu()
    select=int(input("Bienvenido, selecciona(ingresando un numero) cualquiera de las opciones: "))
    num=0
    bin=""
    hex=""
    oct=""
    dec_float=0.0
    suboption=""
    if(select==1):
        print("\n#Convirtiendo un numero Binario a Decimal")
        suboption=input("Ingresa '1' para numero con decimales o ingresa '0' para numero entero: ")
        if(suboption=="1"):
            bin=input("Ingresa tu numero binario con decimales: ")
            dec_float=Bin_Dec_Float(bin)
            print("Tu numero en decimal es: ", dec_float)
        else:
            bin=input("\nIngresa tu numero binario: ")
            num=Bin_Dec(bin)
            print("Tu numero en decimal es:", num)
    elif(select==2):
        print("\n#Covirtiendo un numero Binario a Hexadecimal.")
        suboption=input("Ingresa '1' para numero con decimales o ingresa '0' para numero entero: ")
        if(suboption=="1"):
            bin=input("Ingresa tu numero binario con decimales: ")
            print("Tu numero en hexadecimal es: ", Bin_Hex_Float(bin))
        else:
            bin=input("\nIngresa tu numero binario: ")
            print("Tu numero en hexadecimal es: ", Bin_to_Hex(bin))
    elif(select==3):
        print("\n#Convirtiendo un numero Binario a Octal.")
        suboption=input("Ingresa '1' para numero con decimales o ingresa '0' para numero entero: ")
        if(suboption=="1"):
            bin=input("Ingresa tu numero binario con decimales: ")
            print("Tu numero en octal es: ", Bin_Oct_Float(bin))
        else:
            bin=input("\nIngresa tu numero binario: ")
            print("Tu numero en octal es: ", Bin_to_Oct(bin))
    elif(select==4):
        print("\n#Convirtiendo un numero Decimal a Binario.")
        suboption=input("Ingresa '1' para numero con decimales o ingresa '0' para numero entero: ")
        if(suboption=="1"):
            dec_float=float(input("Ingresa tu numero decimal con parte fraccionaria: "))
            print("Tu numero en binario es: ", Dec_Bin_Float(dec_float))
        else:
            num=int(input("Ingresa tu numero en decimal: "))
            print("Tu numero en binario es igual a:", Dec_Bin(num))
    elif(select==5):
        print("\n#Conviertiendo un numero Decimal a Hexadecimal.")
        suboption=input("Ingresa '1' para numero con decimales o ingresa '0' para numero entero: ")
        if(suboption=="1"):
            dec_float=float(input("Ingresa tu numero decimal con parte fraccionaria: "))
            print("Tu numero en hexadecimal es: ", Dec_Hex_Float(dec_float))
        else:
            num=int(input("Ingresa tu numero decimal: "))     
            print("El numero en hexadecimal es: ", Dec_to_Hex(num)) 
    elif(select==6):
        print("\n#Convirtiendo un numero Decimal a Octal.")
        suboption=input("Ingresa '1' para numero con decimales o ingresa '0' para numero entero: ")
        if(suboption=="1"):
            dec_float=float(input("Ingresa tu numero decimal con parte fraccionaria: "))
            print("Tu numero en octal es: ", Dec_Oct_Float(dec_float))
        else:
            num=int(input("Ingresa tu numero decimal: "))
            print("Tu numero en octal es: ", Dec_to_Oct(num))
    elif(select==7):
        print("\n#Convirtiendo un numero Hexadecimal a Binario.")
        suboption=input("Ingresa '1' para numero con decimales o ingresa '0' para numero entero: ")
        if(suboption=="1"):
            hex=input("Ingresa tu numero hexadecimal con parte fraccionaria: ")
            print("Tu numero en binario es: ", Hex_Bin_Float(hex))
        else:
            hex=input("Ingresa tu numero hexadecimal: ")
            print("Tu numero en binario es: ", Hex_Bin(hex))
    elif(select==8):
        print("\n#Convirtiendo un numero Hexadecimal a Decimal.")
        suboption=input("Ingresa '1' para numero con decimales o ingresa '0' para numero entero: ")
        if(suboption=="1"):
            hex=input("Ingresa tu numero hexadecimal con parte fraccionaria: ")
            print("Tu numero en decimal es: ", Hex_Dec_Float(hex))
        else:
            hex=input("Ingresa tu numero hexadecimal: ")
            print("Tu numero en decimal es: ", Hex_Dec(hex)) 
    elif(select==9):
        print("\n#Convirtiendo un numero Hexadecimal a Octal:")
        suboption=input("Ingresa '1' para numero con decimales o ingresa '0' para numero entero: ")
        if(suboption=="1"):
            hex=input("Ingresa tu numero hexadecimal con parte fraccionaria: ")
            print("Tu numero en octal es: ", Hex_Oct_Float(hex))
        else:
            hex=input("Ingresa tu numero hexadecimal: ")
            print("Tu numero en octal es: ", Hex_Oct(hex))
    elif(select==10):
        print("\n#Convirtiendo un numero Octal a Hexadecimal:")
        suboption=input("Ingresa '1' para numero con decimales o ingresa '0' para numero entero: ")
        if(suboption=="1"):
            oct=input("Ingresa tu numero octal con parte fraccionaria: ")
            print("Tu numero en hexadecimal es: ", Oct_Hex_Float(oct))
        else:
            oct=input("Ingresa tu numero octal: ")
            print("Tu numero en hexadecimal es: ", Oct_Hex(oct))
    elif(select==11):
        print("\n#Convirtiendo un numero Octal a Binario.")
        suboption=input("Ingresa '1' para numero con decimales o ingresa '0' para numero entero: ")
        if(suboption=="1"):
            oct=input("Ingresa tu numero octal con parte fraccionaria: ")
            print("Tu numero en binario es: ", Oct_Bin_Float(oct))
        else:
            oct=input("Ingresa tu numero octal: ")
            bin_aux=Oct_Bin(oct)
            if(bin_aux!=None):
                print("Tu numero en binario es igual a:", bin_aux)
            else:
                print("Numero octal invalido, no puede contener digitos como 8 o 9.")
    elif(select==12):
        print("\n#Convirtiendo un numero Octal a Decimal.")   
        suboption=input("Ingresa '1' para numero con decimales o ingresa '0' para numero entero: ")
        if(suboption=="1"):
            oct=input("Ingresa tu numero octal con parte fraccionaria: ")
            print("Tu numero en decimal es: ", Oct_Dec_Float(oct))
        else:         
            oct=input("Ingresa tu numero octal: ")
            dec_aux=Oct_Dec(oct)
            if(dec_aux!=None):
                print("Tu numero en decimal es igual a:", dec_aux)
            else:
                print("Numero octal invalido, no puede contener digitos como 8 o 9.")
    cont=int(input("¿Quieres seguir ejecutando el programa 1.Si/ 0.No (selecciona ingresando un numero)?: "))
