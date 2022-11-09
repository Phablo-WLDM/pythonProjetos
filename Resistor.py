
def coresResistor3():
    try:
        valoresResistor = []
        NuFaxa = ['PRIMEIRA FAXA!','SEGUNDA FAXA','TERCEIRA FAXA']
        for i in NuFaxa:

                print(i)

                print('\n','SELECINA AS CORES DO RESISTOR!')
                
                cores = int(input(' Preto(0) \n Marrom(1) \n Vermelho(2) \n Laranja(3) \n Amarelo(4) \n Verde(5) \n Azul(6) \n Violetar(7) \n cinza(8) \n Branco(9) \n'))

                if cores == 0:
                    valoresResistor.append(0)

                if cores == 1:
                    valoresResistor.append(1)

                if cores == 2:
                    valoresResistor.append(2)

                if cores == 3:
                    valoresResistor.append(3)

                if cores == 4:
                    valoresResistor.append(4)

                if cores == 5:
                    valoresResistor.append(5)

                if cores == 6:
                    valoresResistor.append(6)

                if cores == 7:
                    valoresResistor.append(7)

                if cores == 8:
                    valoresResistor.append(8)

                if cores == 9:
                    valoresResistor.append(9)
                

                if cores != 0 and cores != 1 and cores != 2 and cores != 3 and cores != 4 and cores !=5 and cores !=6 and cores != 7 and cores != 8 and cores != 9:
                    print('OPIÇAO INVALIDA!')
                    break

    except ValueError:
        print('opição invalida!')

    except IndexError:
        print('Opição Invalida!')

    else:
        for i in range(valoresResistor[2]):
            valoresResistor.append(0)
            
        del valoresResistor[2]
        
        res = str(valoresResistor)[1:-1]
        print(res, 'Ω')





def coresResistor4():
    try:
        valoresResistor = []
        NuFaxa = ['PRIMEIRA FAXA!','SEGUNDA FAXA','TERCEIRA FAXA','QUAL É A TOLERÂNCIA!']
        for i in NuFaxa:

            if i == 'QUAL É A TOLERÂNCIA!':
                print(i)
                tole = int(input('(1)DOURADO! (0)PRATA!'))

                if tole == 1:
                    print('Dourado! selecionado!')

                if tole == 0:
                    print('Prata! selecionado!')

            else:

                print(i)

                print('\n','SELECINA AS CORES DO RESISTOR!')
                
                cores = int(input(' Preto(0) \n Marrom(1) \n Vermelho(2) \n Laranja(3) \n Amarelo(4) \n Verde(5) \n Azul(6) \n Violetar(7) \n cinza(8) \n Branco(9) \n'))

                if cores == 0:
                    valoresResistor.append(0)

                if cores == 1:
                    valoresResistor.append(1)

                if cores == 2:
                    valoresResistor.append(2)

                if cores == 3:
                    valoresResistor.append(3)

                if cores == 4:
                    valoresResistor.append(4)

                if cores == 5:
                    valoresResistor.append(5)

                if cores == 6:
                    valoresResistor.append(6)

                if cores == 7:
                    valoresResistor.append(7)

                if cores == 8:
                    valoresResistor.append(8)

                if cores == 9:
                    valoresResistor.append(9)
                

                if cores != 0 and cores != 1 and cores != 2 and cores != 3 and cores != 4 and cores !=5 and cores !=6 and cores != 7 and cores != 8 and cores != 9:
                    print('OPIÇAO INVALIDA!')
                    break

    except ValueError:
        print('opição invalida!')

    except IndexError:
        print('Opição Invalida!')

    else:
        for i in range(valoresResistor[2]):
            valoresResistor.append(0)
            
        del valoresResistor[2]
        
        res = str(valoresResistor)[1:-1]
        print(res, 'Ω')




def coresResistor5():
    try:
        valoresResistor = []
        NuFaxa = ['PRIMEIRA FAXA!','SEGUNDA FAXA','TERCEIRA FAXA','QUARTA FAIXA','QUAL É TOLERANCIA!']
        for i in NuFaxa:

            if i == 'QUAL É TOLERANCIA!':
                print(i)
                tole = int(input('(1)DOURADO! (0)PRATA!'))

                if tole == 1:
                    print('Dourado! selecionado!')

                if tole == 0:
                    print('Prata! selecionado!')

            else:

                print(i)

                print('\n','SELECINA AS CORES DO RESISTOR!')
                
                cores = int(input(' Preto(0) \n Marrom(1) \n Vermelho(2) \n Laranja(3) \n Amarelo(4) \n Verde(5) \n Azul(6) \n Violetar(7) \n cinza(8) \n Branco(9) \n'))

        

                if cores == 0:
                    valoresResistor.append(0)

                if cores == 1:
                    valoresResistor.append(1)

                if cores == 2:
                    valoresResistor.append(2)

                if cores == 3:
                    valoresResistor.append(3)

                if cores == 4:
                    valoresResistor.append(4)

                if cores == 5:
                    valoresResistor.append(5)

                if cores == 6:
                    valoresResistor.append(6)

                if cores == 7:
                    valoresResistor.append(7)

                if cores == 8:
                    valoresResistor.append(8)

                if cores == 9:
                    valoresResistor.append(9)


                if cores != 0 and cores != 1 and cores != 2 and cores != 3 and cores != 4 and cores !=5 and cores !=6 and cores != 7 and cores != 8 and cores != 9:
                    print('OPIÇAO INVALIDA!')
                    break

    except ValueError:
        print('opição invalida!')
    
    except IndexError:
        print('OPIÇÃO INVALIDA!')

    else:
        for i in range(valoresResistor[3]):
            valoresResistor.append(0)
            
        del valoresResistor[3]
        
        res = str(valoresResistor)[1:-1]
       
        print(res,'Ω')

        
while True:
    try:
        faxa =  int(input('Quantas faixas tem o seu resistor? \n (3)faixa \n (4)faixa \n (5)fixa \n (0)Saír \n'))

        if faxa == 3:
            coresResistor3()

        if faxa == 4:
            coresResistor4()
        
        if faxa == 5:
            coresResistor5()
        

        if faxa == 0:
            break

        
    except ValueError:
        print('OPIÂO INVALIDA!')