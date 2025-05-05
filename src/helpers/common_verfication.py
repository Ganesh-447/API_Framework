#Http Verification



def verify_http_code(response_data,expect_data):
    assert response_data.status_code == expect_data, f"Expected HTTP status code {expect_data}, but got {response_data.status_code}"


def verify_json_key_not_null(key):
    assert key !=0 , "Key should be non zero"+key
    #assert key > 0 , "key should be greater than zero"

def verify_response(key):
    assert key is not None, f'{key} should not be None'

def verify_single_field(response_data,field_key,expected_value):
    assert field_key in response_data , f"Field {field_key} is not found in response data"
    assert response_data[field_key] == expected_value , f"Field '{field_key}' value is not as expected. Expected: {expected_value}, but got: {response_data[field_key]}"


def respone_time():
    pass



#Common Verfication

#HTTP Status code
#Headers
#Data verfication.
#