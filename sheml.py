#!/usr/bin/python3
import os
import cheemthon

while True:
    text = input("(*´∇`)ﾉ > ")
    if text.strip() == "cmlear":
        os.system('clear' if os.name == 'posix' else 'cls')
        continue
    if text.strip() == "":
        continue
    result, error = cheemthon.run("<stdin>", text)

    if error:
        print(error.as_string())
    elif result:
        if len(result.elements) == 1:
            print(repr(result.elements[0]))
        else:
            print(repr(result))