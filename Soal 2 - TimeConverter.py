def timeConverter(seconds):
    a=seconds//3600
    b=(seconds%3600)//60
    c=(seconds%3600)%60
    d=print("Konversi {}:{}:{}".format(a, b, c))
    return d

e = int(input('Masukkan Detik : '))
timeConverter(e)