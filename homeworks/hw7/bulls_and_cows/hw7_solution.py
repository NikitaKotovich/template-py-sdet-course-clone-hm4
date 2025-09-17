import random


def check_guess(users: str, computer: str) -> tuple:
    bull = 0
    cow = 0
    for us in users:
        for co in computer:
            if us == co and users.index(us) == computer.index(us):
                bull += 1
            elif us == co and users.index(us) != computer.index(us):
                cow += 1
    bull_cow = (bull, cow)
    return bull_cow


def generate_secret_number() -> str:
    secret = ''
    while len(secret) < 4:
        hz = str(random.randint(0, 9))
        if hz not in secret:
            secret += hz
    return secret
