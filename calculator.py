Donkey = 0
while True:
    Shrek = input(Donkey)
    if Shrek[1:].isnumeric():
        if Shrek[0] == "-":
            Shrek = 19999 - int(Shrek[1:])
            for ad in range(Shrek):
                Donkey += 1
                if Donkey == 10000:
                    Donkey = -9999
        elif Shrek[0] == "+":
            Shrek = int(Shrek[1:])
            for haha_nerd in range(Shrek):
                Donkey += 1
                if Donkey == 10000:
                    Donkey = -9999
        elif Shrek[0] == "x":
            if Shrek[1:] in ["0", "1"]:
                if Shrek[1:] == "0":
                    Donkey = 0
            else:
                if Donkey > 0:
                    Shrek = int(Shrek[1:]) - 1
                    Lord_Farquaad = Donkey
                    for who_actually_reads_variable_names in range(Shrek):
                        for count in range(Lord_Farquaad):
                            Donkey += 1
                            if Donkey == 10000:
                                Donkey = -9999
                elif Donkey < 0:
                    Shrek = int(Shrek[1:]) - 1
                    Lord_Farquaad = -Donkey
                    for who_actually_reads_variable_names in range(Shrek):
                        I_dare_you_to_understand_my_code = 19999 - int(Lord_Farquaad)
                        for count in range(I_dare_you_to_understand_my_code):
                            Donkey += 1
                            if Donkey == 10000:
                                Donkey = -9999
        else:
            print("Huh?")
    else:
        print("Huh?")
