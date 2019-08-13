import statistics as es

hitoria_n1 = float(input('Digite a primeira nota: '))
hitoria_n2 = float(input('Digite a segunda nota:  '))

lista_notas = [hitoria_n1,hitoria_n2]
media = es.mean(lista_notas)

if media >= 7:
    print('aprovado')

elif media >= 5 and media < 7:
    print('recuperação')

else: print ('reprovado')   

