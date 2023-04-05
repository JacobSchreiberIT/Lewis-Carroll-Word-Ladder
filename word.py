class word:
    Lewis_Carroll_distance = 0
    Different_letters = 0
    new_word = ""

    def __lt__(self, other):
        if (word.Lewis_Carroll_distance + word.Different_letters) < (other.Lewis_Carroll_distance + other.Different_letters):
            return True
        elif (word.Lewis_Carroll_distance + word.Different_letters) == (other.Lewis_Carroll_distance + other.Different_letters):
            if word.Lewis_Carroll_distance < other.Lewis_Carroll_distance:
                return True
        return False

    def __eq__(self, other):
        if word.Lewis_Carroll_distance == other.Lewis_Carroll_distance and word.Different_letters == other.Different_letters:
            return True
        return False
    
    def get_LCD(self):
        return word.Lewis_Carroll_distance
    
    def set_LCD(self, x):
        word.Lewis_Carroll_distance = x
    
    def get_diff_letters(self):
        return word.Different_letters
    
    def set_diff_letters(self, x):
        word.Different_letters = x

    def get_new_word(self):
        return word.new_word

    def set_new_word(self, x):
        word.new_word = x
    