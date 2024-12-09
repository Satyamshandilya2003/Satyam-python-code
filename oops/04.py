from random import randint

class Train:

    def __init__(self,trainNo):
        self.trainNo = trainNo

    def book(self,fro ,to):
        print(f"Ticket is booked in the train no:{self.trainNo} from {fro}to {to}")

    def getStatus(self):
        print(f"train no:{self.trainNo} is running on the time")

    def getFare(self,fro,to):
        print (f"Ticket is fare  in train no:{self.trainNo} from {fro} to {to} is {randint(222,5555)}")

t = Train(12345)
t.book("Rampur","Delhi")
t.getStatus("Rampur","Delhi")
t.getFare("Rampur","Delhi")