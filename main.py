from corporateData import CorporateData
from corporateLog import CorporateLog

if __name__ == "__main__":
    corporate_data = CorporateData()
    corporate_log = CorporateLog()

    uuid = "12345"
    sede = "Sede Central"

    data = corporate_data.getData(uuid, sede)
    corporate_log.post(uuid, "getData")
    print(data)

    cuit = corporate_data.getCUIT(uuid, sede)
    corporate_log.post(uuid, "getCUIT")
    print(cuit)

    seq_id = corporate_data.getSeqID(uuid, sede)
    corporate_log.post(uuid, "getSeqID")
    print(seq_id)