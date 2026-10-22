#11-misol
class User:
    def __init__(self, username):
        self.username = username

u1 = User("alim")
u2 = User("sara")
u1.username = "alim007"
print(u1.username)
print(u2.username)

#12-misol
class Good:
    def __init__(self):
        self.items = []

g1 = Good()
g2 = Good()
g1.items.append(1)
print(g2.items)
