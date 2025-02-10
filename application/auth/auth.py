import requests


class TokenAuth(requests.auth.AuthBase):
    def __init__(self, token_url, client_id, client_secret):
        self.token_url = token_url
        self.client_id = client_id
        self.client_secret = client_secret
        self.token = self.get_new_token()

    def get_new_token(self):
        response = requests.post(self.token_url,
                                 data={"client_id": self.client_id, "client_secret": self.client_secret},
                                 headers={"Content-Type": "application/x-www-form-urlencoded"})
        response.raise_for_status()
        return response.json()["access_token"]

    def __call__(self, request):
        request.headers["Authorization"] = f"Bearer {self.token}"
        return request

    def refresh_token(self):
        print("Refreshing token...")
        self.token = self.get_new_token()


class AutoRefreshAdapter(requests.adapters.HTTPAdapter):
    def __init__(self, auth, session, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.auth = auth
        self.session = session

    def send(self, request, **kwargs):
        response = super().send(request, **kwargs)
        if response.status_code == 401:
            print("401 detected, refreshing token...")
            self.auth.refresh_token()
            new_token = f"Bearer {self.auth.token}"
            self.session.headers.update({"Authorization": new_token})
            request.headers["Authorization"] = new_token
            print(f"Retrying request with new Authorization header: {request.headers.get('Authorization')}")
            return super().send(request, **kwargs)

        return response

