messages=["Hi","Welcome to platform","OK"]
for message in messages:
    length=len(message)
    print(f"Message: {message} has length: {length}")

    if length>10:
        print("This is a long message.")
    