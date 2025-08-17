#code for 100 vehicle parking[python and mysql.]
from . import sqltest

class Parkings:
    def __init__(self):

        self.p=sqltest.Server()

    def park(self,carno):

        print("these are the available slots",self.p.find())
        slot= self.p.find()
        for slots,car in slot :

            if len(carno) == 10:
                pass

                if car == "free":

                    self.p.park1(carno,slots)

                else:
                    continue
            else:
                print("not a valid no,redo it")

            print("\nCar parked at slot no:",self.p.find())
            break

        if all(k=="occupied" for k in slot):
                print("\nparking is full")
                print("\n no available slots")

    def depart(self,carex):

        print('occupied slots',self.p.find())


        slot = self.p.find()
        for slots,car in slot:

            if len(carex) == 10:
                if car == carex:
                    self.p.exit1(slots)
                else:

                 continue
        print("Empty slots",self.p.find())

def main():

    q = Parkings()
    while True:

        no=int(input("\n1:park\n2:depart\n3.quit app\nenter a val:"))
        match no:
            case 1:
                carno=str(input("enter the car no"))
                q.park(carno)

            case 2:
                carex = str(input("Enter car no"))
                q.depart(carex)

            case 3:
                print("quit applicaiton")
                break

if __name__ == "__main__":
    main()








