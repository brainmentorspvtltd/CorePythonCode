def login(func):
    print("Login Function Called...")
    return func

@login
def post():
    print("Let's Post Something...")


def message():
    print("Do Message...")

# message()
post()