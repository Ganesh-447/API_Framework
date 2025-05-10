import requests
import pytest

from src.constants.api_constants import create_auth,patch_put_delete,create_booking
from src.helpers.api_request_wrapper import post_request,put_request,delete_request
from src.helpers.utils import common_header_json
from src.helpers.payload_manager import payload_auth,payload_create_booking,payload_update_booking
from src.helpers.common_verfication import verify_http_code,verify_json_key_not_null,verify_response,verify_single_field
from tests.integration_test.conftest import token,booking_id

class TestCrud:

    def test_create_token(self,token):
        print(f'token {token}')

    def test_create_booking(self,booking_id):
        print(f'booking_id is {booking_id}')



    def test_update_full_booking(self,token,booking_id):
        put_url = patch_put_delete(booking_id)
        headers = common_header_json()
        headers["Cookie"] = f"token={token}"
        update_pay_load = payload_update_booking()
        update_response = put_request(url=put_url,auth=None,headers=headers,payload=update_pay_load)
        verify_http_code(update_response,200)
        updated_data = update_response.json()
        verify_single_field(response_data=updated_data,field_key="firstname",expected_value="Ganesh")
        print(updated_data)
        #return headers

    def test_delete_booking(self,booking_id,token):
        delete_url=patch_put_delete(booking_id)
        header = common_header_json()
        header["Cookie"] = f'token={token}'
        delete_booking = delete_request(url=delete_url,auth=None,headers=header)
        verify_http_code(delete_booking,201)
        print(f'your booking id {booking_id} is deleting')
        print(delete_booking)
