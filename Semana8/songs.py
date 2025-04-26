with open ("sons.txt", "w") as file:
    file.write("No woman, no cry\n")
    file.write("I believe to my soul\n")
    file.write("Free birds\n")
    file.write("If i Ain´t got you\n")

print ("The file has been create with successfully")

with open ("sons.txt", "r") as file:
    song= file.readlines()

song.sort()

with open ("sons_sorted.txt", "w") as file:
    file.writelines(song)
print ("The songs are been sorted and saved in 'sons_sorted.txt' .")