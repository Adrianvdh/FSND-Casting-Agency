from unittest import mock

token_response = mock.MagicMock(return_value='AAAAAAA.BBBBB.CCCCC')

casting_assistant_payload = mock.MagicMock(return_value={
    'iss': 'https://testserver/',
    'sub': 'google-oauth2|123',
    'aud': 'AAA',
    'iat': 1619856220,
    'exp': 1619942620,
    'azp': 'CCCCC',
    'scope': 'openid profile email',
    'permissions': [
        'get:actor-detail',
        'get:actors',
        'get:movie-detail',
        'get:movies'
    ]
})

casting_director_payload = mock.MagicMock(return_value={
    'iss': 'https://testserver/',
    'sub': 'google-oauth2|123',
    'aud': 'AAA',
    'iat': 1619856220,
    'exp': 1619942620,
    'azp': 'CCCCC',
    'scope': 'openid profile email',
    'permissions': [
        'delete:actors',
        'get:actor-detail',
        'get:actors',
        'get:movie-detail',
        'get:movies',
        'patch:actors',
        'patch:movies',
        'post:actors'
    ]
})

executive_producer_payload = mock.MagicMock(return_value={
    'iss': 'https://testserver/',
    'sub': 'google-oauth2|123',
    'aud': 'AAA',
    'iat': 1619856220,
    'exp': 1619942620,
    'azp': 'CCCCC',
    'scope': 'openid profile email',
    'permissions': [
        'delete:actors',
        'delete:movies',
        'get:actor-detail',
        'get:actors',
        'get:movie-detail',
        'get:movies',
        'patch:actors',
        'patch:movies',
        'post:actors',
        'post:movies'
    ]
})
