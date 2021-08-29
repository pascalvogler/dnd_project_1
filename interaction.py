import assemble_source_data


def initiate_interaction(source):
    input("Press any key to start")
    print("First we will pick a race")
    print("There are the available races:")
    for race in source.races:
        print(race['name'])

