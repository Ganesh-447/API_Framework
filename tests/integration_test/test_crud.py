import requests
import pytest

from src.constants.api_constants import create_auth,patch_put_delete,create_booking
from src.helpers.api_request_wrapper import post_request,put_request
from src.helpers.utils import common_header_json
from src.helpers.payload_manager import payload_auth,payload_create_booking
from src.helpers.common_verfication import verify_http_code,verify_json_key_not_null,verify_response

class TestCrud:


    def test_create_token(self):
        token_response = post_request(url=create_auth(),auth= None, headers=common_header_json(),payload=payload_auth())
        verify_http_code(token_response, 200)
        verify_response(token_response)
        #print(token_response.json()["token"])
        token= token_response.json()["token"]
        verify_json_key_not_null(token)
        print(token)
        return token

    def test_create_booking(self):
        create_response = post_request(url=create_booking(),auth= None ,headers=common_header_json(),payload=payload_create_booking())
        #print(create_response)
        verify_http_code(create_response,200)
        booking_id = create_response.json()["bookingid"]
        verify_json_key_not_null(booking_id)
        print(booking_id)
        return booking_id

    def test_update_full_booking(self):
        update_response = put_request(url=patch_put_delete(self.test_create_booking()),auth=self.test_create_token())


    def test_delete_booking(self):
        pass
