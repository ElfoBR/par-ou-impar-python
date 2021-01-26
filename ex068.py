from random import randint
c = 0
while True:
    je = str(input('quer par ou impar?(p/i) '))
    pc = randint(1, 10)
    j = int(input('insira seu numero: '))
    s = j + pc
    print(f'computador jogou {pc} e vc {j}, o resultado foi {s}')
    if je == 'p':
        if s % 2 == 0:
            print('ganhou')
        else:
            print('perdeu')
            break
    if je == 'i':
        if s % 2 == 1:
            print('ganhou')
        else:
            print('perdeu')
            break
    if je != 'i' and je != 'p':
        print('opção invalida')
    c += 1
print(f'ganhou {c} vezes')
            