import json
from typing import List


class AccessDb:

    assets = None

    def __init__(self):
        if not AccessDb.assets:
            with open('scripts/assets.json', 'r') as f:
                AccessDb.assets = json.load(f)


class SearchTerm:

    def __init__(self, terms: str, types: str, tags: str):
        self.terms: List[str] = self.resolve(terms)
        self.types: List[str] = self.resolve(types)
        self.tags: List[str] = self.resolve(tags)
        self.meta_data: [object]

    @staticmethod
    def resolve(input: str):
        if input == '':
            return []
        else:
            return input.split(' ')


def search(search_term: SearchTerm):

    def match(st: SearchTerm, asset) -> bool:

        if st.terms:
            for term in st.terms:
                if term not in asset.get('name', ''):
                    return False

        if st.types:
            if asset.get('type') not in st.types:
                return False

        if st.tags:
            for tag in st.tags:
                if tag not in asset.get('tags', ''):
                    return False

        return True

    return (asset for asset in AccessDb().assets if match(search_term, asset))


if __name__ == '__main__':
    db = AccessDb()
    for asset in search(SearchTerm(terms='generic window', types='mesh bitmap', tags='chair prop')):
        print(asset.get('type'), asset.get('name'), asset.get('tags'))
