import requests
import pytest
import allure
from src.helpers.api_request_wrapper import post_request
from src.constants.api_constants import create_booking
from src.helpers.utils import common_header_json
from src.helpers.payload_manager import payload_create_booking
from src.helpers.common_verfication import verify_response, verify_http_code

@allure.epic("Booking API Tests")
@allure.feature("Create Booking")
class TestCreateBooking:

    @allure.story("Create Booking with valid data")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description("Test to create booking with valid data and verify response contains booking and firstname keys")
    @pytest.mark.positive
    def test_create_booking_tc1(self):
        response = post_request(
            url=create_booking(),
            auth=None,
            headers=common_header_json(),
            payload=payload_create_booking()
        )
        verify_http_code(response, 200)

        try:
            response_json = response.json()
        except Exception as E:
            pytest.fail(f"Response is not valid JSON: {E}")

        assert 'booking' in response_json, f"'booking' key missing in response: {response_json}"
        assert 'firstname' in response_json['booking'], f"'firstname' key missing in booking: {response_json['booking']}"
        verify_response(response_json["booking"]["firstname"])
        print(response_json["bookingid"])

    @allure.story("Create Booking with empty payload")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.description("Test to create booking with empty payload and expect server to return 500 error")
    @pytest.mark.negative
    def test_create_booking_tc2(self):
        response = post_request(
            url=create_booking(),
            auth=None,
            headers=common_header_json(),
            payload={}
        )
        print(response)
        verify_http_code(response, 500)
