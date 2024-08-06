class Musica:
    nome = ''
    artista = ''
    duracao = int

musica1 = Musica()
musica1.nome = 'Nothing att all'
musica1.artista = 'Air Supply'
musica1.duracao = 355

musica2 = Musica()
musica2.nome = 'With or Without You'
musica2.artista = 'U2'
musica2.duracao = 386

musica3 = Musica()
musica3.nome = 'Free Bird'
musica3.artista = 'Lynyrd Skynyrd'
musica3.duracao = 381

print(f'Música: {musica1.nome} - Banda: {musica1.artista} - Duração: {musica1.duracao} seg')
print(f'Música: {musica2.nome} - Banda: {musica2.artista} - Duração: {musica2.duracao} seg')
print(f'Música: {musica3.nome} - Banda: {musica3.artista} - Duração: {musica3.duracao} seg')