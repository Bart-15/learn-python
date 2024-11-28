# Create a dictionary called cool_dictionary where you use words for keys and definitions for values

words = ["Sus","Spange","Lie-Fi"]
definitions = ["Suspicious","To collect spare change, either from couches, passerbys on the street or any numerous other ways and means","When your phone or tablet indicates that you are connected to a wireless network, however you are still unable to load webpages or use any internet services with your device"]

# using dict() and zip()
result1 = dict(zip(words, definitions))

print(result1)

# using loop
result2 = {words[i]: definitions[i] for i in range(min(len(words), len(definitions)))}
print(result2)