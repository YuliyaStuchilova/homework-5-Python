# Создайте программу для игры в ""Крестики-нолики"".


dask = [1, 2, 3,
        4, 5, 6,
        7, 8, 9]


def print_dask():
    print(dask[0],dask[1],dask[2])
    print(dask[3],dask[4],dask[5])
    print(dask[6],dask[7],dask[8])


print_dask()

s=''
for i in range(9):
    if i%2==0:
        print('Ходит игрок 1')
        s='X'
        number=int(input('выберите позицию для хода: '))
        dask[number-1]=s
        print_dask()

    else:
        print('Ходит игрок 2')
        s='0'
        number=int(input('выберите позицию для хода: '))
        dask[number-1]=s
        print_dask()

if dask[0]==dask[1]==dask[2]=='0':
    print('Победил Игрок 2')
if dask[0]==dask[1]==dask[2]=='X':
    print('Победил Игрок 1')
if dask[3]==dask[4]==dask[5]=='0':
    print('Победил Игрок 2')
if dask[3]==dask[4]==dask[5]=='X':
    print('Победил Игрок 1')
if dask[6]==dask[7]==dask[8]=='0':
    print('Победил Игрок 2')
if dask[6]==dask[7]==dask[8]=='X':
    print('Победил Игрок 1')
if dask[0]==dask[3]==dask[6]=='0':
    print('Победил Игрок 2')
if dask[0]==dask[3]==dask[6]=='X':
    print('Победил Игрок 1')
if dask[1]==dask[4]==dask[7]=='0':
    print('Победил Игрок 2')
if dask[1]==dask[4]==dask[7]=='X':
    print('Победил Игрок 1')
if dask[2]==dask[5]==dask[8]=='0':
    print('Победил Игрок 2')
if dask[2]==dask[5]==dask[8]=='X':
    print('Победил Игрок 1')
if dask[0]==dask[4]==dask[8]=='0':
    print('Победил Игрок 2')
if dask[0]==dask[4]==dask[8]=='X':
    print('Победил Игрок 1')
if dask[2]==dask[4]==dask[6]=='0':
    print('Победил Игрок 2')
if dask[2]==dask[4]==dask[6]=='X':
    print('Победил Игрок 1')