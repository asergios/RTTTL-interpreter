#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os



def val_nota(v):
    if(v!=1 and v!=2 and v!=4 and v!=8 and v!=16 and v!=32):
        print("ERRO Nº4 - Valor da nota inválido!")
        return False
    return True


def main(demo):
    #demo = "The Simpsons:d=4,o=5,b=160:c.6,e6,f#6,8a,g.6,e6,c6,8a,8f#,8f#,8f#,2g,8p,8p,8f#,8f#,8f#,8g,a#.,8c6,8c6,8c6,c6"
    demo = demo.split(":")
    
    
    if(len(demo)!=3):
		print("ERRO Nº1 - Pauta mal construida")
		return "ERRO Nº1 - Pauta mal construida"
    
    title = demo[0]
    referencias = demo[1]
    pauta = demo[2]
    
    #########################################################################3
    
    # Referencias PARSE VVVVVVV
    referencias = referencias.split(",")
    
    if(len(referencias)!=3):
        if(len(referencias)<3):
            if(len(referencias)==0):
                d=4
                o=6
                b=63
            if(len(referencias)==2):
                if(referencias[0][0]=="d" and referencias[1][0]=="o"):
                    d = int(referencias[0][2:])
                    if(val_nota(d)!= True):
			            return
                    o = int(referencias[1][2:])
                    b = 63
                if(referencias[0][0]=="o" and referencias[1][0]=="b"):
                    d = 4
                    o = int(referencias[0][2:])
                    b = int(referencias[1][2:])
                if(referencias[0][0]=="d" and referencias[1][0]=="b"):
                    d = int(referencias[0][2:])
                    if(val_nota(d)!= True):
			            return
                    o = 6
                    b = int(referencias[1][2:])
                else:
					print("ERRO Nº3 - Referencias invalidas")
					return "ERRO Nº3 - Referencias invalidas"
            else:
                if(referencias[0][0]=="d"):
                    d = int(referencias[0][2:])
                    if(val_nota(d)!= True):
			            return 
                    o = 6
                    b = 63
                if(referencias[0][0]=="o"):
                    d = 4
                    o = int(referencias[0][2:])
                    b = 63
                if(referencias[0][0]=="b"):
                    d = 4
                    o = 6
                    b = int(referencias[1][2:])
                else:
					print("ERRO Nº3 - Referencias invalidas")
					return "ERRO Nº3 - Referencias invalidas"
        else:
		    print("ERRO Nº2 - Demasiadas referencias")
		    return "ERRO Nº2 - Demasiadas referencias"
    else:
        d = int(referencias[0][2:])
        if(val_nota(d)!= True):
	        return 
        o = int(referencias[1][2:])
        b = int(referencias[2][2:])
        
        
    ################################################################# 
    
    # Construtor de freq[] VVVVVV
    
    n = -9
    freq = [] 
    
    for tom in range(0, 108):
        freq.insert(tom, int(440 * pow(2,n/float(12))))
        if(n!=50):
            n +=1
        else:
			n = -57

    #################################################################
    # Pauta PARSE e Escrita do ficheiro VVVVVV
    
    indx = ['c', 'c#', 'd', 'd#', 'e', 'f', 'f#', 'g', 'g#', 'a', 'a#', 'b', 'p']
    
    pares_file = open(os.path.join("pares", title.replace(" ","")+"-notes.txt"), 'w')
    pares_file.write("[ ")
    notas = pauta.split(",")
    
    for n in range(0, len(notas)):
        escala = o
		## Valor da nota e calculo do tempo (ainda sem o ponto)
        if(notas[n][0].isdigit()):
            try:
                if(val_nota(int(notas[n][:2]))!= True):
                    return
                tempo = (4/float(notas[n][:2])) * (60/float(b))
            except:
                if(val_nota(int(notas[n][0]))!= True):
                    return
                tempo = (4/float(notas[n][0])) * (60/float(b))
            
            ## Nota
            if(len(notas[n])>2):
                if(notas[n][2] == "#"):
                    try:
                        nota = indx.index(notas[n][1:3])					
                    except:
					    print("ERRO Nº5 - Nota inválida")
					    return "ERRO Nº5 - Nota inválida"
					    
					# Ponto / Oitava
                    if(len(notas[n])>3):
                         if(notas[n][3] == "."):
                             tempo =  tempo * 1.5
                             if(len(notas[n])>4):
                                 if(notas[n][4].isdigit()):
                                     if(int(notas[n][4])>=0 and int(notas[n][4])<=8):
                                         escala = int(notas[n][4])	
                                     else:
                                         print("ERRO Nº6 - Escala inválida")
                                         return	"ERRO Nº6 - Escala inválida"								 
                         else: 					
                             if(notas[n][3].isdigit()):
                                 if(int(notas[n][3])>=0 and int(notas[n][3])<=8):
                                     escala = int(notas[n][3]) 
                                 else:
                                    print("ERRO Nº6 - Escala inválida")	
                                    return "ERRO Nº6 - Escala inválida"	  								 
                else:
                    try:
                        nota = indx.index(notas[n][1])					
                    except:
                        try:
                            nota = indx.index(notas[n][2])
                        except:	
                            print("ERRO Nº5 - Nota inválida")
                            return "ERRO Nº5 - Nota inválida"
                        
                    # Ponto / Oitava    
                    if(notas[n][2] == "."):
                        tempo =  tempo * 1.5
                        if(len(notas[n])>3):
                            if(notas[n][3].isdigit()):
                                if(int(notas[n][3])>=0 and int(notas[n][3])<=8):
                                    escala = int(notas[n][3])
                                else:
                                    print("ERRO Nº6 - Escala inválida")
                                    return "ERRO Nº6 - Escala inválida"						 
                    else: 					
                        if(notas[n][2].isdigit()):
                            if(int(notas[n][2])>=0 and int(notas[n][2])<=8):
                                escala = int(notas[n][2])
                            else:
                                    print("ERRO Nº6 - Escala inválida")
                                    return "ERRO Nº6 - Escala inválida"	
            else:
                try:
                    nota = indx.index(notas[n][1])					
                except:
                    print("ERRO Nº5 - Nota inválida")
                    return "ERRO Nº5 - Nota inválida"
                    
   ###################################################         
        else:
            tempo = (4/float(d)) * (60/float(b))
                
            if(len(notas[n])>1):
                if(notas[n][1] == "#"):
                    try:
                        nota = indx.index(notas[n][0:2])					
                    except:
					    print("ERRO Nº5 - Nota inválida")
					    return "ERRO Nº5 - Nota inválida"
					    
					# Ponto / Oitava
                    if(len(notas[n])>2):
                         if(notas[n][2] == "."):
                             tempo =  tempo * 1.5
                             if(len(notas[n])>3):
                                 if(notas[n][3].isdigit()):
                                     if(int(notas[n][3])>=0 and int(notas[n][3])<=8):
                                         escala = int(notas[n][3])	
                                     else:
                                         print("ERRO Nº6 - Escala inválida")
                                         return	"ERRO Nº6 - Escala inválida"								 
                         else: 					
                             if(notas[n][2].isdigit()):
                                 if(int(notas[n][2])>=0 and int(notas[n][2])<=8):
                                     escala = int(notas[n][2]) 
                                 else:
                                    print("ERRO Nº6 - Escala inválida")	
                                    return "ERRO Nº6 - Escala inválida"	  								 
                else:
                    try:
                        nota = indx.index(notas[n][0])					
                    except:
                        print("ERRO Nº5 - Nota inválida")
                        return "ERRO Nº5 - Nota inválida"
                        
                    # Ponto / Oitava    
                    if(notas[n][1] == "."):
                        tempo =  tempo * 1.5
                        if(len(notas[n])>2):
                            if(notas[n][2].isdigit()):
                                if(int(notas[n][2])>=0 and int(notas[n][2])<=8):
                                    escala = int(notas[n][2])
                                else:
                                    print("ERRO Nº6 - Escala inválida")
                                    return "ERRO Nº6 - Escala inválida"							 
                    else: 					
                        if(notas[n][1].isdigit()):
                            if(int(notas[n][1])>=0 and int(notas[n][1])<=8):
                                escala = int(notas[n][1])
                            else:
                                    print("ERRO Nº6 - Escala inválida")
                                    return "ERRO Nº6 - Escala inválida"			
            else:
                try:
                    nota = indx.index(notas[n][0])					
                except:
                    print("ERRO Nº5 - Nota inválida")
                    return "ERRO Nº5 - Nota inválida"
        if(nota!=12):            
            pares_file.write("("+str(round(tempo, 3))+", "+str(freq[12*(escala-4)+nota])+"), \n") 
        else:
            pares_file.write("("+str(round(tempo,3))+", 0), \n")             

    pares_file.write(" ]")    
    pares_file.close()
    
    return "Sucess"
    
    ##################################################################
		

    
    
