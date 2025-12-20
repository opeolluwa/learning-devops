def hello():
    print("Yo fam")


def betterHello(name):
    print(f"hey mane {name}")
    return name 


hello()
betterHello("alex")

alex = betterHello("alex")
print(alex)


def spam(divideBy):
    try:
        return 42 / divideBy
    except ZeroDivisionError:
        print("error")

print(spam(2))
print(spam(12))
print(spam(0))
print(spam(1))