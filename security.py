import rsa

def generate_keys():
    public_key, private_key = rsa.newkeys(512)
    return public_key, private_key
