'''Verifica strings de tamanhos iguais e destaca diferenças entre [] com várias ocorrências'''

def ver(fa,fb):
    fna, fnb = '', ''
 
    for i in range(len(fa)):
        if fa[i] != fb[i]:
            fna += f'[{fb[i]}]'
            fnb += f'[{fa[i]}]'
            continue
        
        fna += fa[i]
        fnb += fa[i]

    return fna + fnb

assert ver('abcd','accb') == 'a[c]c[b]a[b]c[d]'

assert all((ver('kj','lj') == '[l]j[k]j',
            ver('oo','io') == '[i]o[o]o',
            ver('ab','bb') == '[b]b[a]b'))

assert all((ver('oi','oy') == 'o[y]o[i]',
            ver('ab','ac') == 'a[c]a[b]',
            ver('aa','ab') == 'a[b]a[a]',))

assert all((ver('b','c') == '[c][b]',
            ver('1','2') == '[2][1]',
            ver('a','b') == '[b][a]'))