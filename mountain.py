#make a dictionary with five mountains with therir height
mountains = {"Everest" : "8858", "k2" : "8611", "Makaalu" : "8485", "K5" : "8080", "K3" : "8051"}
#print the name of the mountains
for mountain in mountains:
	print(mountain)
#print the height of the mountains
for mountain in mountains:
	print(mountains[mountain])
#print the name of the muontains with their heights
sorted(mountains)
for mountain in mountains:
	print(mountain + " is " + mountains[mountain] + " meters tall")
def feet(height):
	n_feet = height * 3.28
	print("Hight in feet: " + n_feet)
mountains_1 = {"mount everest": {"elevation": 8848, "range": "himalaya"}, "k2": {"elevation": 8611, "range": "karakoram"}, "kangchenjunga":  {"elevation": 8586, "range": "himalaya"}, "Lhotse": {"elevation": 8516, "range": "himalaya"}, "Makalu": {"elevation": 8462, "range": "himalaya"}}
print("This mountains are very huge:")
for mountain in mountains_1 :
     print(mountain.title())
print("\n..and here there dare their elevations:")
for mountain in mountains_1 :
    print(mountains_1 [mountain]["elevation"])

print("\n..and here's the range they belong to:")
for mountain in mountains_1 :
    print(mountains_1 [mountain]["range"].title())

for mountain in mountains_1 :
    print("%s is an %d-meter tall mountain in the %s range." % (mountain, mountains_1 [mountain]["elevation"], (mountains_1 [mountain]["range"]).title()))