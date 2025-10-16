from datetime import datetime

def get_timestamp():
    """Return current timestamp in readable format"""
    return datetime.now().strftime("%d-%b-%Y %H:%M:%S")


if __name__=="__main__":
    print(get_timestamp())