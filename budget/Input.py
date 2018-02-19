class Input():
    def ask_for_category(self, key):
        return input('What category does %s belong in? ' % key)

    def ask_for_key(self, description):
        print('\n%s' % description)
        if len(description) > 15:
            return input('Assign a key: ')
        else:
            return description
    
    def determine_key_and_category(self, description):
        key = self.ask_for_key(description)
        category = self.ask_for_category(key)
        return key, category
