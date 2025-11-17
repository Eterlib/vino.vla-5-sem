class Sender:
    first = True

    def report(self):
        if Sender.first:
            print("Greetings!")
            Sender.first = False
        else:
            print("Get away!")


class Asker:
    def askall(self, lst):
        for x in lst:
            x.report()
