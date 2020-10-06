songs = ["ROCKSTAR", "Do It", "For The Night"]

print(songs[1:])

songs[2] = "It's The End Of The World As We Know It"

print(songs)

songs.append("Last Train Home")

songs.extend(["il vento d'oro"])

songs.insert(0, "Stand Proud")

songs.pop(1)

print(songs)

for song in songs:
 print(song)

for i in range(len(songs)):
 print(songs[i])

animals = ["Cat", "Dog", "Bird"]

animals.insert(3, "Giraffe")

print(animals[2])

animals.pop(0)

for animal in animals:
    print(animal)




