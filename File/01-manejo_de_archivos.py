liked_songs = {
    "Smells Like Teen Spirit": "Nirvana",
    "Wonderwall": "Oasis",
    "Black": "Pearl Jam",
    "Alive": "Pearl Jam",
    "November Rain": "Guns N' Roses",
    "Enter Sandman": "Metallica",
    "Losing My Religion": "R.E.M."
}

def write_liked_songs_to_file(liked_songs, file_name):
    
    with open(file_name, 'w') as file:
        file.write('Liked Songs:\n')
        for song, artis in liked_songs.items():
            (file.write(f'{song} by {artis}\n'))

write_liked_songs_to_file(liked_songs, 'mi_musica.txt')

