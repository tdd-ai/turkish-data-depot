from datetime import timedelta
import traceback
import getpass
import requests
import os

if getpass.getuser() in ["root", "www-data"]:
	from .prod import *
else:
	from .dev import *

CONFIG_DIR = os.path.join(Path(BASE_DIR).parent, 'config')
JWT_PUBLIC_KEY_PATH = os.path.join(CONFIG_DIR, 'jwt_key.pub')

if not os.path.exists(CONFIG_DIR):
    os.makedirs(CONFIG_DIR)

if not DEBUG:
	try:
		pem_public = requests.get("https://auth.tdd.ai/fetch-public-key").json()["key"]
		with open(JWT_PUBLIC_KEY_PATH, 'w') as pk:
			pk.write(pem_public)

		print("Public Key fetched")
	except Exception as e:
		traceback.print_exc()

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=60),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=7),
    'ROTATE_REFRESH_TOKENS': False,

    'ALGORITHM': 'RS256',
    'SIGNING_KEY': None,
    'VERIFYING_KEY': open(JWT_PUBLIC_KEY_PATH).read(),
    'AUDIENCE': None,
    'ISSUER': None,

    'AUTH_HEADER_TYPES': ('Bearer',),
    'USER_ID_FIELD': 'id',
    'USER_ID_CLAIM': 'user_id',

    'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',),
    'TOKEN_TYPE_CLAIM': 'token_type',

    'JTI_CLAIM': 'jti',
}
