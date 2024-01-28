### ALBUM

albuns = []

def func_make_album(n_artista, n_album, n_faixas):
    dic = {'artista':n_artista, 'album':n_album, 'faixas': n_faixas }
    albuns.append(dic)


while True:
    print('\n---- Realizando Pesquisa ----')
    artista = input('\nDigite artista: ')
    if artista == 'q':
        break
    album = input('\nDigite Album: ')
    if album == 'q':
        break
    faixas = input('\nNumero de faixas: ')
    if faixas == 'q':
        break

    func_make_album(artista, album, faixas)

print(albuns)

for album in albuns:
    print('-'*100)
    print('\n\t Album: ')
    for k, v in album.items():
        print('\t\t' + k.title() + ':', v.title())

