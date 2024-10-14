class CorporateData:
    _instance = None
    sequence_id = 0

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(CorporateData, cls).__new__(cls)
            cls._init_data()
        return cls._instance

    @classmethod
    def _init_data(cls):
        cls.address = "Calle 345"
        cls.cuit = "30-12345678-9"
        cls.phone_number = "+5493442345678"

    def getData(self, uuid, sede):
        return {"sede": sede, "Domicilio": self.address, "Localidad": "Concepcion del Uruguay", "Cp": "3260", "provincia": "Entre Ríos"}

    def getCUIT(self, uuid, sede):
        return {"sede": sede, "CUIT": self.cuit}

    def getSeqID(self, uuid, sede):
        self.sequence_id += 1
        return {"sede": sede, "seqID": self.sequence_id}