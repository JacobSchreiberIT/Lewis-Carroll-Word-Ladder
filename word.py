class word:
    _Lewis_Carroll_distance = 0
    _Different_letters = 0
    _new_word = ""

    def __lt__(self, other):
        if (word._Lewis_Carroll_distance + word._Different_letters) < (other._Lewis_Carroll_distance + other._Different_letters):
            return True
        elif (word._Lewis_Carroll_distance + word._Different_letters) == (other._Lewis_Carroll_distance + other._Different_letters):
            if word._Lewis_Carroll_Distance < other._Lewis_Carroll_Distance:
                return True
        return False

    def __eq__(self, other):
        if word._Lewis_Carroll_distance == other._Lewis_Carroll_distance and word._Different_letters == other._Different_letters:
            return True
        return False
    
    def get_LCD():
        return word._Lewis_Carroll_distance
    
    def set_LCD(self, x):
        word._Lewis_Carroll_distance = x
    
    def get_diff_letters():
        return word._Different_letters
    
    def set_diff_letters(self, x):
        word._Different_letters = x
    