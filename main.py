''' Verificador de diferenças de string '''

''' Verifica em strings de mesmo tamanho'''

''' Verifica strings de tamanhos diferentes com apenas 1 ocorrência'''

def ver(fa,fb):
    novafb, novafa, difsa, difsb = '','', '', ''
    try:
        if len(fa) > len(fb):
            for i in range(len(fa)):
                
                if fa[i] != fb[i]:
                    difsa += fa[i]
                    difsb += fb[i]
                    continue

                if difsa and difsb:
                    novafa += f'[{difsa}]' + fa[i] 
                    novafb += f'[{difsb}]' + fb[i]
                    difsa, difsb = '', ''
                else:
                    novafa += f'{difsa}' + fa[i] 
                    novafb += f'{difsb}' + fb[i]

        else:
            for i in range(len(fb)):
                
                if fb[i] != fa[i]:
                    difsa += fa[i]
                    difsb += fb[i]
                    continue
                
                if difsa and difsb:
                    novafa += f'[{difsa}]' + fa[i] 
                    novafb += f'[{difsb}]' + fb[i]
                    difsa, difsb = '', ''
                else:
                    novafa += f'{difsa}' + fa[i] 
                    novafb += f'{difsb}' + fb[i]
                
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

    if difsa:
        return novafa + f'[{difsb}]' + novafb + f'[{difsa}]'
    else:
        return novafa + novafb

assert all((ver('abcd','abef') == 'ab[ef]''ab[cd]',
            ver('olae','olea') == 'ol[ea]''ol[ae]',
            ver('xyzw','xywz') == 'xy[wz]''xy[zw]'))

assert all((ver('abcd','abc') == 'abc[]''abc[d]',
            ver('123','1234') == '123[4]''123[]',
            ver('olá?','olá') == 'olá[]''olá[?]'))

assert all((ver('ab','ac') == 'a[c]''a[b]',
            ver('12','13') == '1[3]''1[2]',
            ver('oi','oy') == 'o[y]''o[i]'))

assert all((ver('a','b') == '[b]''[a]',
            ver('c','d') == '[d]''[c]',
            ver('e','f') == '[f]''[e]'))