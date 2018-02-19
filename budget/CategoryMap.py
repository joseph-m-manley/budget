class CategoryMap():
    def __init__(self, dictOfLists = dict()):
        self.d = dictOfLists
        self.keywords = {x for _list in dictOfLists.values() for x in _list}

    def __eq__(self, other):
        if not isinstance(other, CategoryMap):
            raise TypeError()
        for category in self.d:
            if category not in other:
                return False
            if sorted(self.d[category]) != sorted(other[category]):
                return False
        return True

    def __contains__(self, item):
        return item in self.d

    def __delitem__(self, item):
        del self.d[item]

    def __len__(self):
        return len(self.d)

    def __iter__(self):
        for x in self.d:
            yield x

    def __getitem__(self, category):
        return self.d[category]

    def get(self, category):
        return self.d[category]

    def __safe_get(self, category):
        if category not in self.d:
            self.d[category] = []
        return self.d[category]

    def add(self, category, keyword):
        c, k = category.lower(), keyword.lower()
        self.__safe_get(category).append(keyword)
        self.keywords.add(keyword)

    def keyword_exists(self, description):
        for keyword in self.keywords:
            if keyword in description:
                return True
        return False

    def to_json(self):
        return self.d

