import assemble_source_data
import interaction

def start_creation():
    source = assemble_source_data.Sources.introduction()
    print('sdf')
    interaction.initiate_interaction(source)



if __name__ == '__main__':
    start_creation()

