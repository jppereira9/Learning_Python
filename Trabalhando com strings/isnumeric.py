'''
Os métodos isdigit e isnumeric são parecidos, e diferenciá-los envolve um conhecimento de Unicode mais 
aprofundado. isdigit retorna true para caracteres definidos como dígitos numéricos em Unicode, indo além
de nossos 0 a 9, como o número 9 tibetano 9 (\u0f29). isnumeric é mais abrangente, incluindo dígitos e
representações númericas como frações, por exemplo, 1/3 (\u2153). Vejamos alguns exemplos:

'''

umterco = "\u2153"
novetibetano = "\u0f29"
print(f'{umterco.isdigit()}')
print(f'{umterco.isnumeric()}')
print(f'{novetibetano.isnumeric()}')
print(f'{novetibetano.isdigit()}')
