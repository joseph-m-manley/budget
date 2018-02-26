class Input():
    def ask_for_category(self, key):
        return input('What category does \'%s\' belong in? ' % key).upper()

    def ask_for_key(self, description):
        print('\n%s' % description)
        if len(description) <= 15:
            return description        
        key = input('Assign a key: ')
        if key == '':
            key = description
        return key.upper()
    
    def determine_key_and_category(self, description):
        key = self.ask_for_key(description)
        category = self.ask_for_category(key)
        return key, category
