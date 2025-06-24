class Firm:
    __firm_name = ''
    __firm_owner = ''
    __firm_address = ''
    __firm_sphere = ''
    __firm_phone = ''

    def __init__(self, firm_name: str, firm_owner: str, firm_address: str, firm_sphere: str, firm_phone: str):
        self.__firm_name = firm_name
        self.__firm_owner = firm_owner
        self.__firm_address = firm_address
        self.__firm_sphere = firm_sphere
        self.__firm_phone = firm_phone

    def __str__(self) -> str:
        text = (f"Firm name: {self.__firm_name}\n"
                f"Firm owner: {self.__firm_owner}\n"
                f"Firm address: {self.__firm_address}\n"
                f"Firm sphere: {self.__firm_sphere}\n"
                f"Firm phone: {self.__firm_phone}\n\n")
        return text

    def getFirmName(self) -> str:
        return self.__firm_name

    def getFirmOwner(self) -> str:
        return self.__firm_owner

    def getFirmAddress(self) -> str:
        return self.__firm_address

    def getFirmSphere(self) -> str:
        return self.__firm_sphere

    def getFirmPhone(self) -> str:
        return self.__firm_phone

    def setFirmName(self, firm_name):
        self.__firm_name = firm_name

    def setFirmOwner(self, firm_owner):
        self.__firm_owner = firm_owner

    def setFirmAddress(self, firm_address):
        self.__firm_address = firm_address

    def setFirmSphere(self, firm_sphere):
        self.__firm_sphere = firm_sphere

    def setFirmPhone(self, firm_phone):
        self.__firm_phone = firm_phone