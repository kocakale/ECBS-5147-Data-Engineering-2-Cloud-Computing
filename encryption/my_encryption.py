# %%
from pathlib import Path

from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA

PROJECT_FOLDER = Path(__file__).parent.parent
PRIVATE_KEY_FILE = PROJECT_FOLDER / "my_keypair"
PUBLIC_KEY_FILE = PROJECT_FOLDER / "my_keypair.pub"

assert Path.exists(PRIVATE_KEY_FILE)
assert Path.exists(PUBLIC_KEY_FILE)