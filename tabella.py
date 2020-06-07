#!/usr/bin/env/python3
import pickle


class Table:
    def __init__(self):
        self.players = []
        return

    def find_by_name(self, name):
        for p in self.players:
            if p.name == name:
                return p
        return None

    def add_player(self, name):
        for p in self.players:
            if p.name == name:
                raise ValueError("Ilyen jatekos mar letezik.")
        self.players.append(Player(name))
        return

    def print_table(self):
        info = []
        goals = []
        for p in self.players:
            info.append(p.get_printable())
            goals.append(p.goals)
        info = reversed([x for _, x in sorted(zip(goals, info))])
        print("{0:20s}{1:10s}{2:10s}".format("Nev", "Meccsek", "Golok"))
        print("========================================")
        for i in info:
            print(i)
        print("========================================")
        return

    def save(self):
        fout = open("Tabella", "wb")
        pickle.dump(self, fout)
        fout.close()
        return

    def load(self):
        fin = open("Tabella", "rb")
        saved = pickle.load(fin)
        fin.close()
        return saved


class Player:
    def __init__(self, name):
        self.name = name
        self.goals = 0
        self.games = 0
        return

    def update(self):
        print("Hany meccset szeretnel hozzaadni? Jelenleg {0:s} {1:d} meccsel all.".format(self.name, self.games))
        try:
            game = input().strip()
            self.games += int(game)
        except ValueError:
            print("Helytelen formatum, a frissites sikertelen.")
            return
        print("Hany golt szeretnel hozzaadni? Jelenleg {0:s} {1:d} gollal all.".format(self.name, self.goals))
        try:
            goal = input().strip()
            self.goals += int(goal)
        except ValueError:
            print("Helytelen formatum, a frissites sikertelen.")
            return
        return

    def get_printable(self):
        return "{0:20s}{1:10d}{2:10d}".format(self.name, self.games, self.goals)


if __name__ == '__main__':
    t = Table()
    try:
        t = t.load()
    except FileNotFoundError:
        pass
    while True:
        print("Tabella: t\nFrissites: f\nKilepes: q\n")
        ans = input().strip()
        if ans == "q":
            t.save()
            break
        elif ans == "t":
            t.print_table()
        elif ans == "f":
            print("Adj meg egy nevet:")
            name = input().strip()
            p = t.find_by_name(name)
            if p is None:
                print("Nincs ilyen jatekos, szeretnel hozzaadni? y/*")
                ans2 = input().strip()
                if ans2 == "y":
                    t.add_player(name)
            else:
                p.update()
