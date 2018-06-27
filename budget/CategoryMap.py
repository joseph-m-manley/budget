class CategoryMap():
    def __init__(self, intializerDict = dict()):
        self.d = dict()
        self.keywords = set()
        for category in intializerDict:
            self.d[category] = list()
            for keyword in intializerDict[category]:
                self.add(category, keyword)

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

    def __get_or_make_category(self, category):
        if category not in self.d:
            self.d[category] = []
        return self.d[category]

    def add(self, category, keyword):
        category = category.lower()
        keyword = keyword.lower()
        self.__get_or_make_category(category).append(keyword)
        self.keywords.add(keyword)

    def keyword_exists(self, description):
        for keyword in self.keywords:
            if keyword.lower() in description.lower():
                return True
        return False

    def to_json(self):
        return self.d

