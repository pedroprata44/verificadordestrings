''' Verificador de diferenças de string '''

''' Verifica em strings de mesmo tamanho'''

''' Verifica strings de tamanhos diferentes'''

def ver(fa,fb):

    novafb, novafa, difs = '', '', ''

    try:
        if len(fa) > len(fb):
            for i in range(len(fa)):
                if fa[i] == fb[i]:
                    novafa += fa[i] 
                    novafb += fb[i]
                else:
                    novafa += f'[{fb[i]}]' 
                    novafb += f'[{fa[i]}]'
        else:
            for i in range(len(fb)):
                if fb[i] == fa[i]:
                    novafa += fa[i] 
                    novafb += fb[i]
                else:
                    novafa += f'[{fb[i]}]'
                    novafb += f'[{fa[i]}]'

    except IndexError:
        dif = 0
        if len(fa) > len(fb):
            dif = len(fa) - len(fb)
            novafb += f'[{fa[-dif:]}]'
            novafa += '[]'
        else:
            dif = len(fb) - len(fa)
            novafa += f'[{fb[-dif:]}]'
            novafb += '[]'
    
    return novafa + novafb

assert ver('abcd','abc') == 'abc[]''abc[d]'
assert ver('123','1234') == '123[4]''123[]'
assert ver('olá?','olá') == 'olá[]''olá[?]'

assert all((ver('ab','ac') == 'a[c]''a[b]',
            ver('12','13') == '1[3]''1[2]',
            ver('oi','oy') == 'o[y]''o[i]'))

assert all((ver('a','b') == '[b]''[a]',
            ver('c','d') == '[d]''[c]',
            ver('e','f') == '[f]''[e]'))