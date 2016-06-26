#
names = ["name1", "neme2", "name3", "name4"]

def crowd_test():
    if len(names) >= 5:
        print("there is a mob in the room")
    elif len(names) >= 3:
		print("the room is crowded")
    elif len(names) >= 1:
		print("the room is not very crowded ")
    else:
        print("the room is empty")

del names[-1]
del names[-1]
crowd_test()
names.extend(["name5", "name6"])


