data_dict = {
    "eaa99349": [
        {
            "type": "DEPOSIT",
            "amount": 1000,
            "date": "18-Oct-2025 12:53:34",
            "remark": "Account Opening Amount",
        },
        {
            "type": "DEPOSIT",
            "amount": 1000,
            "date": "18-Oct-2025 12:56:33",
            "remark": "Account Opening Amount",
        }
    ],
    "fdaa6e94": [
        {
            "type": "DEPOSIT",
            "amount": 169.0,
            "date": "18-Oct-2025 13:24:35",
            "remark": "Account Opening Amount",
        }
    ],
    "b8222fb9": [
        {
            "type": "DEPOSIT",
            "amount": 69.0,
            "date": "18-Oct-2025 14:50:46",
            "remark": "Account Opening Amount",
        }
    ]
}


for key, value in data_dict.items():
    for li in value:
            print(f"""
            "encrypted id" : {key},
            "Type": {li["type"]}
            "Amount":{li["amount"]} 
            "Date": {li["date"]}
            "Remark": {li["remark"]},

""")
