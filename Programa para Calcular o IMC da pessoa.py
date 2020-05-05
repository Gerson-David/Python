# Programa para calcular o índice de massa corporal da pessoa!(IMC)

peso = float(input('Digite seu peso (Kg): '))
altu = float(input('Digite sua altura: '))
imc = peso / (altu ** 2)
print('O IMC dessa pessoa é de {:.1f}'.format(imc))
if imc < 18.5:
    print('Você está ABAIXO DO PESO normal!')
elif imc >= 18.5 and imc < 25:
    print('Parabéns, você está na faixa de PESO NORMAL!')
elif imc >= 25 and imc < 30:
    print('Você está em SOBREPESO')
elif imc >= 30 and imc < 40:
    print('ATENÇÃO, Você está com OBESIDADE')
else:
    print('CUIDADO, você está com OBESIDADE MORBIDA!')