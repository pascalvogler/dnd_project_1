import assemble_source_data


def initiate_interaction(source):
    input("Press any key to start")
    print("First we will pick a race")
    print("These are the available races:")
    print("---")
    i = 0
    for race in source.races:
        print(f"{race['name']} [{i}]")
        i += 1
    valid_race_info = False
    while not valid_race_info:
        input_race_info = input("Do you already know which race (yes)? Nood more info (no)? ")
        if input_race_info == 'yes':
            valid_race_info = True
        elif input_race_info == 'no':
            input_race_info_index = int(input("Type the index number you wish to have more information about: "))
            source.get_race_info(input_race_info_index)
        else:
            print(f"{input_race_info} is not a valid answer here.")

    input_race_choice = input("Type in the number of your desired race then: ")

