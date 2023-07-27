"""
The private key is build by two prime numbers 'p' and 'q'
This method askes the user 'Alice' for two numbers. They should be atleast 1024 bit to be secure.
"""
def create_private_key():
    p = int(input("Enter the first private prime: "))
    q = int(input("Enter the second private prime: "))
    return {'p':p, 'q':q}

"""
The public key is the sum of the two primes 'p' and 'q'.
At encryption time a third prime 'e' is needed. 
"""
def create_public_key(private):
    N = private['p'] * private['q']
    e = int(input("Enter the public prime: "))
    return {'N':N, 'e': e}

"""
To be able to decode the message, the two private primes 'p' and 'q' are needed together with the public one 'e'.
A third number, the decryption key 'd' is also needed.
The formula to get 'd' is e*d = 1 (mod(p-1)*(q-1))
"""
def calculate_decryption_key(private, public):
    private['d'] = 23
    return private

"""
To sign a message you encrypt it with your private key instead of using the public key.
Everybody with access to you public key will be able to decrypt this message. This proves that you are the person you say that you are.
"""
def sign_message(private, raw_message):
    None

"""
To be able to encrypt a message you use the receivers public key.
In this way only the person with the corresponding private key can decode the message.
The message 'M' needs to be a binary number that you get by convert the text with ASCII character per character.
The formula to encrypt is C = M^e (mod N) where 'C' is the encrypted message and 'e' and 'N' comes from the receivers public key. 
"""
def encrypt(pub, raw_message):
    return ord(raw_message) ** pub['e'] % pub['N']

"""
To decrypt a message you need your two private primes 'p' and 'q' along with the decryption key. 
The formula for decryption is M = C^d (mod N)
"""
def decrypt(private, encrypted_message):
    return chr(encrypted_message ** private['d'] % (private['p'] * private['q']))

if __name__ == "__main__":
    alice_pk = create_private_key()
    print(f"The first private prime is {alice_pk['p']} and the second is {alice_pk['q']}")
    alice_pub = create_public_key(alice_pk)
    print(f"The encryption key is {alice_pub['e']} and the public key is  {alice_pub['N']}")
    alice_pk = calculate_decryption_key(alice_pk, alice_pub)
    message = str(input("Bob, Enter the character you want to send: "))
    encrypted = encrypt(alice_pub, message)
    print(f"The message was {message} and it was encrypted to {encrypted}")
    print(f"Alice got the message {decrypt(alice_pk, encrypted)}")