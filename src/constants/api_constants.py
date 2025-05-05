


Base_API = "https://restful-booker.herokuapp.com"

def create_booking():

    return f"{Base_API}/booking"

def create_auth():

    return f"{Base_API}/auth"

def patch_put_delete(booking_id):

    return f"{Base_API}/booking/{booking_id}"
