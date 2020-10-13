import rsa
import base64

(pub_key, private_key) = rsa.newkeys(512)


def check_rsa():
    message = b'Hello World!'
    crypto = rsa.encrypt(message, pub_key)
    print(crypto)
    message = rsa.decrypt(crypto, private_key)
    print(message)


def encrypt_rsa_with_base64(message: str) -> bytes:
    crypto = rsa.encrypt(message.encode(), pub_key)
    return base64.b64encode(crypto)


def decrypt_rsa_with_base64(crypto: bytes) -> str:
    raws = base64.b64decode(crypto)
    return str(rsa.decrypt(raws, private_key))


if __name__ == '__main__':
    crypto_message = encrypt_rsa_with_base64('Hello world!')
    print(crypto_message)
    print(decrypt_rsa_with_base64(crypto_message))

