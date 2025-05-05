def payload_create_booking():

    payload={
    "firstname" : "Jim",
    "lastname" : "Brown",
    "totalprice" : 111,
    "depositpaid" : True,
    "bookingdates" : {
        "checkin" : "2018-01-01",
        "checkout" : "2019-01-01"
    },
    "additionalneeds" : "Breakfast"
}
    return payload

def payload_auth():
    payload_token ={
        "username": "admin",
        "password": "password123"
        }
    return payload_token

def payload_update_booking():

    payload_update = {
    "firstname" : "Ganesh",
    "lastname" : "Grandhi",
    "totalprice" : 111,
    "depositpaid" : True,
    "bookingdates" : {
        "checkin" : "2018-01-01",
        "checkout" : "2019-01-01"
    },
    "additionalneeds" : "Dinner"
}
    return payload_update