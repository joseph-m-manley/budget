class Input():
    def ask_for_category(self, key):
        return input('What category does %s belong in? ' % key).lower()

    def ask_for_key(self, description):
        print('\n%s' % description)
        key = description
        if len(key) > 15:
            x = input('Assign a key? ').lower()
            if x not in ('Y', 'N', ''):
                key = x
            elif x == 'Y':
                key = input('Key: ').lower()
        return key
    
    def determine_key_and_category(self, description):
        key = self.ask_for_key(description)
        category = self.ask_for_category(key)
        return key, category
