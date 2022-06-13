class Student():
    # [assignment] Skeleton class. Add your code here
    def __init__(self, name, age, tracks, score):
        self.name = "Jay"
        self.age = age
        self.tracks = tracks
        self.score = 99.99
        print("My name is",name, "\nI am",age, "years old" "\nI offer", tracks,"\nAnd this is my score:",score)

    def change_name(self):
        new_name = input("Change the name: ")
        print(new_name)

    def change_age(self):
        new_age = input("Change the age: ")
        print(new_age)

    def add_track(self):
        next_track = input("What other tracks are you in?: ")
        self.tracks.extend([next_track])
        print(self.tracks)

    def get_score(self):
        print("This is your score - ",self.score)

Bob = Student('Jay', 26, ["FT","FS"], 2)
Bob

# Expected methods
Bob.change_name()
Bob.change_age()
Bob.add_track()
Bob.get_score()