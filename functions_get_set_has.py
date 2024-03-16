class Example:
    pass


e = Example()

while True:
    attr = input("Give me attribute name ")
    value = input("Give me attribute values ")

    setattr(e, attr, value)

    print(dir(e))

    if hasattr(e, "test"):
        print('Object{} has attribute with value {}'.format(e, getattr(e, "test")))
    else:
        print('Object{} does not have attribute with value {}'.format(e, getattr(e, "test")))