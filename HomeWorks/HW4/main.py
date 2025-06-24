from Equilibrium import Equilibrium
from Firm import Firm


def main():
    f1 = Firm("test1", "tester1", "tests street1",
              "testing", "+3812341234")

    f2 = Firm("test2", "tester2", "tests street2",
              "testing2", "+387777777")

    f3 = Firm("test3", "tester3", "tests street3",
              "testing3", "+386666666")

    firms = [f1, f2, f3]

    eq = Equilibrium(firms)
    print("orig:")
    eq.showContents()
    print(eq.deleteFirm(
        firm=eq.findFirmByName("test1")
    ))

    print("deleted:")
    eq.showContents()

    eq.addFirm(f1)
    print("add:")
    eq.showContents()


if __name__ == "__main__":
    main()