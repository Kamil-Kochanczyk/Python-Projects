"""
Napisać program pobierający w pętli od użytkownika liczbę rzeczywistą x (typ float) i wypisujący x oraz trzecią potęgę x.
Zatrzymanie programu następuje po wpisaniu z klawiatury stop.
Jeżeli użytkownik wpisze napis zamiast liczby, to program ma wypisać komunikat o błędzie i kontynuować pracę.
"""

user_input = None
stop = "stop"

while user_input != stop:
    user_input = input("Enter a real number x: ")
    try:
        x = float(user_input)
        print(f"x = {x}")
        print(f"x^3 = {x * x * x}")
    except ValueError:
        if user_input != stop:
            print("Error: wrong input type")
            print("Input should be a real number")
    finally:
        print("\n--------------------\n")