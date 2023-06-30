'''Verifica strings de tamanhos iguais e destaca diferenças entre [] com várias ocorrências'''

def ver(fa,fb):
    novafa, novafb, desta, destb = '', '', '', ''

    for i in range(len(fa)):
        if fa[i] != fb[i]:
            desta += fb[i]
            destb += fa[i]

            if i == range(len(fa))[-1]:
                novafa += f'[{desta}]'
                novafb += f'[{destb}]'
            
            continue

        if desta != '':
            novafa += f'[{desta}]{fa[i]}'
            novafb += f'[{destb}]{fa[i]}'
            desta, destb = '', ''
            continue

        novafa += fa[i]
        novafb += fa[i]

    return f'{novafa + novafb}'

assert all((ver('oo','ii') == '[ii][oo]',
            ver('ll','mm') == '[mm][ll]',
            ver('aa','bb') == '[bb][aa]'))

assert all((ver('kj','lj') == '[l]j[k]j',
            ver('oo','io') == '[i]o[o]o',
            ver('ab','bb') == '[b]b[a]b'))

assert all((ver('oi','oy') == 'o[y]o[i]',
            ver('ab','ac') == 'a[c]a[b]',
            ver('aa','ab') == 'a[b]a[a]',))

assert all((ver('b','c') == '[c][b]',
            ver('1','2') == '[2][1]',
            ver('a','b') == '[b][a]'))