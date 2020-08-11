from apiclient import discovery
import httplib2
from oauth2client import client

# (Receive auth_code by HTTPS POST)


def get_google_user_details(request, code):
    # If this request does not have `X-Requested-With` header, this could be a CSRF

    # Set path to the Web application client_secret_*.json file you downloaded from the
    # Google API Console: https://console.developers.google.com/apis/credentials
    CLIENT_SECRET_FILE = '/Users/sushant/work/Projects/confidently/pocs/confidently_auth_api/client_secret.json'

    # Exchange auth code for access token, refresh token, and ID token
    credentials = client.credentials_from_clientsecrets_and_code(
        CLIENT_SECRET_FILE,
        ['profile', 'email'],
        code)

    # Get profile info from ID token

    # Returned Data Format [credentials.id_token]
    '''
        at_hash: "Kxfu7ZIRaQIEhrOf_6YU0Q"
        aud: "126580856541-o521m1umrmc2iv48jl0nsdnjlbuagcc3.apps.googleusercontent.com"
        azp: "126580856541-o521m1umrmc2iv48jl0nsdnjlbuagcc3.apps.googleusercontent.com"
        email: "vsushant97@gmail.com"
        email_verified: true
        exp: 1597190214
        family_name: "Vangapandu"
        given_name: "Sushant"
        iat: 1597186614
        iss: "https://accounts.google.com"
        locale: "en"
        name: "Sushant Vangapandu"
        picture: "https://lh3.googleusercontent.com/a-/AOh14GggK79ulXGWlbl6hGN06TveDFHHYe9AdKzNrXOx=s96-c"
        sub: "106640096938816490795"
    '''
    userid = credentials.id_token['sub']
    email = credentials.id_token['email']

    return {"user_id": userid, "email": email, "additional": credentials.id_token}
