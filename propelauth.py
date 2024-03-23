from propelauth_py import init_base_auth, UnauthorizedException
from streamlit.web.server.websocket_headers import _get_websocket_headers
import requests

class Auth:
    def __init__(self, auth_url, integration_api_key):
        self.auth = init_base_auth(auth_url, integration_api_key)
        self.auth_url = auth_url
        self.integration_api_key = integration_api_key

    def get_user(self):
        access_token = get_access_token()

        if not access_token:
            return None

        try:
            return self.auth.validate_access_token_and_get_user("Bearer " + access_token)
        except UnauthorizedException as err:
            print("Error validating access token", err)
            return None

    def get_account_url(self):
        return self.auth_url + "/account"
    
    def logout(self):
        refresh_token = get_refresh_token()
        if not refresh_token:
            return False

        logout_body = {"refresh_token": refresh_token}
        url = f"{self.auth_url}/api/backend/v1/logout"
        headers = {
            "Content-Type": "application/json",
            "Authorization": "Bearer " + self.integration_api_key,
        }
        
        response = requests.post(url, json=logout_body, headers=headers)
        
        return response.ok


def get_access_token():
    return get_cookie("__pa_at")

def get_refresh_token():
    return get_cookie("__pa_rt")

def get_cookie(cookie_name):
    headers = _get_websocket_headers()
    if headers is None:
        return None

    cookies = headers.get("Cookie") or headers.get("cookie") or ""
    for cookie in cookies.split(";"):
        split_cookie = cookie.split("=")
        if len(split_cookie) == 2 and split_cookie[0].strip() == cookie_name:
            return split_cookie[1].strip()

    return None

auth = Auth(
    "https://72027091.propelauthtest.com",
    "122c53ac14528fe26f3975fcbd480427dce11ac656ff143aec236fd0da851cff31e3bc19b93847dba976f182fd838c8a"
)
