def http_status(status):
    match status:
        case 200:
            return "ok"
        case 404:
            return "Not Found"
        case 500:
            return "Internal Server Error"
        case _:
            return "Unknown status" #Usuage Print(http_status(200)) #output : Ok print(http_status(404)) #Output : Not Found Print(http_status(500)) #Output : Internal Server

print(http_status(500))