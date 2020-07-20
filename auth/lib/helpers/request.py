def get_access_token_from_request(request):
    authorization = request.headers.get('Authorization')
    authorization = authorization.split(' ')[1]
    return authorization
