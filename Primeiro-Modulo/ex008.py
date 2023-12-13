# Leia um valor em metros e mostre o valor em centímetros e milímetros.
v = float(input('Digite um valor em metros: '))
print('{}m equivale a {}cm e {}ml'.format(v, v*100, v*1000))


n = float(input('Digite outro valor em metros: '))
km = (n / 1000)
hm = (n / 100)
dam = (n / 10)
m = n
dm = (n * 10)
cm = (n * 100)
mm = (n * 1000)
print('Tabela: \n{}Km \n{}hm \n{}dam \n{}m \n{}dm \n{}cm \n{}mm'.format(km, hm, dam, m, dm, cm, mm))
