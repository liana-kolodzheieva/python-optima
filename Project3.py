q=int(input('How much will you put in the bank?: '))
w=int(input('What amount do you want to receive?: '))
p=int(input('Enter the banks interest rate: '))
k=0
qw=q
while (qw<=w):
    qp = qw*p/100
    qw=qw+qp
    print('Amount in the bank: ', round(qw, 2))
    k+k+1
    print('Year: ', k)
print('Necessary ', k, ' year(s)')
input('Press Enter to exit')