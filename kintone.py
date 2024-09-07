import json
import urequests as requests

def uploadRecord(*, subDomain: str, apiToken: str, record: dict):
    url = "https://" + subDomain + ".kintone.com/k/v1/record.json"
    headers = {"X-Cybozu-API-Token": apiToken,
               "Content-Type": "application/json"}
    response = requests.post(url, headers=headers, json=record)
    if response.status_code == 200 and "id" in json.loads(response.text):
        print("Record uploaded.", end=" ")
        recordId = json.loads(response.text)["id"]
        print("Record ID: " + recordId)
        return recordId
    else:
        print("Record upload failed. Status code: " + str(response.status_code))
        return None
