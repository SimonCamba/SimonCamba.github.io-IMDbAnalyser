import csv

data=[]
with open("IMDB-Movie-Data.csv",newline="") as mycsv:
 foglio=csv.reader(mycsv)
 for row in foglio:
  data.append(row)
print(f"Il file contiene {len(data)} righe")
print(f"L'intestazione del file è: {data[0]}")

l_rating=[float(row[8]) for row in data[1:]]
for row in data[1:]:
 if float(row[8])==max(l_rating):
  print(f"La pellicola col Rating maggiore è: {row[1]}")

actor_frequencies = {}
attori = row[5].split(',')
for actor in attori:
 actor = actor.strip()
 if actor in actor_frequencies:
   actor_frequencies[actor] += 1
 else:
  actor_frequencies[actor] = 1

actor_with_max_movies = max(actor_frequencies, key=actor_frequencies.get)
print(f"L'attore che ha partecipato in un maggior numero di film è: {actor_with_max_movies}")

def FilmERatingXRegista(director):
 film = []
 rating_tot = 0.0
 n_film = 0
 for row in data[1:]:
  if row[4] == director:
   film.append(row[1])
   rating_tot += float(row[8])
   n_film += 1
 if n_film > 0:
  rating_medio = rating_tot / n_film
 else:
  rating_medio = 0.0

 print(f"Il rating medio del regista {director} è: {rating_medio}")
 return film

nuovi_dati = [['Director', 'Movie', 'Average Rating']]
registi = set(row[4] for row in data[1:])

for director in registi:
    director_movies = FilmERatingXRegista(director)
    rating_medio = 0.0
    n_film = 0
    for row in data[1:]:
        if row[1] in director_movies:
            rating_medio += float(row[8])
            n_film += 1
    if n_film > 0:
        rating_medio /= n_film
    nuovi_dati.append([director, ', '.join(director_movies), rating_medio])

with open('FilmXRegista.csv', 'w', newline='') as file:
    scrittore = csv.writer(file)
    scrittore.writerows(nuovi_dati)
