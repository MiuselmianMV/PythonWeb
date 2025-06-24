from typing import List

from Firm import Firm


class Equilibrium:
    __firms_lst: List[Firm] = []
    __file_path = './info.txt'

    def __init__(self, firms: List[Firm]):
        self.__firms_lst = firms
        with open(self.__file_path, 'w', encoding='utf-8') as f:
            for firm in self.__firms_lst:
                f.write(f"{self.__firms_lst.index(firm)}\n")
                f.write(firm.__str__())


    def addFirm(self, firm: Firm):
        self.__firms_lst.append(firm)
        with open(self.__file_path, 'a+', encoding='utf-8') as f:
            f.write(f"{self.__firms_lst.index(firm)}\n")
            f.write(firm.__str__())

    def deleteFirm(self, firm: Firm|None):
        if firm is None:
            return "FirmNotFound"
        try:
            self.__firms_lst.remove(firm)
        except ValueError:
            return "FirmNotFound"

        with open(self.__file_path, 'w', encoding='utf-8') as f:
            for firm in self.__firms_lst:
                f.write(f"{self.__firms_lst.index(firm)}\n")
                f.write(firm.__str__())

        return "FirmDeleted successfully"

    def findFirmByName(self, firm_name: str) -> Firm | None:
        for firm in self.__firms_lst:
            if firm.getFirmName() == firm_name:
                return firm
        else:
            return None

    def findFirmByOwner(self, firm_owner: str) -> Firm | None:
        for firm in self.__firms_lst:
            if firm.getFirmOwner() == firm_owner:
                return firm
        else:
            return None

    def findFirmBySphere(self, firm_sphere: str) -> Firm | None:
        for firm in self.__firms_lst:
            if firm.getFirmSphere() == firm_sphere:
                return firm
        else:
            return None

    def findFirmByPhone(self, firm_phone: str) -> Firm | None:
        for firm in self.__firms_lst:
            if firm.getFirmPhone() == firm_phone:
                return firm
        else:
            return None

    def showContents(self) -> None:
        with open(self.__file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()

        for line in lines:
            print(line)
