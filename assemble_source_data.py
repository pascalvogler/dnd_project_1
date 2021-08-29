import json


class Sources:
    def __init__(self, source_list):
        self.source_list = source_list
        print('Adding playable races...')
        self.races = self.filter_by_source_id('data/races.json')
        print('Adding feats...')
        self.feats = self.filter_by_source_id('data/feats.json')

    @classmethod
    def introduction(cls):
        print("Hello adventurer. Let's create a character for you.")
        print("Which source books do you want to have included?")
        print("All the official ones. Good!")
        with open('data/books.json') as b:
            book_data = json.load(b)
        return cls([b.get('id', 'NO ID INCLUDED') for b in book_data['book'] if b.get('author', '') == "Wizards RPG Team"])

    def filter_by_source_id(self, file_path):
        with open(file_path) as f:
            raw_data = json.load(f)
            if file_path == 'data/races.json':
                data_filtered_by_source = [race for race in raw_data['race'] if race.get('source') in self.source_list]
                data_filtered_by_playable = [race for race in data_filtered_by_source if 'NPC Race' not in race.get('traitTags', [])]
                return data_filtered_by_playable
            elif file_path == 'data/feats.json':
                return [feat for feat in raw_data['feat'] if feat.get('source') in self.source_list]
