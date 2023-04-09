from queue import PriorityQueue
from word import word

def convert(s1, s2, wordset):
    convert_list = list()
    if s1 == s2:
        return "Entered words already equal each other"
    
    if len(s1) != len(s2):
        return "Entered words are different lengths, conversion is not possible"

    priority_queue = PriorityQueue(maxsize=0)
    word_dict = dict()
    word_dict[s1] = "///"
    word_obj = word()
    word_obj.set_new_word(s1)
    priority_queue.put(word_obj)
    while_bool = True
    outer_bool = False

    while(while_bool):
        if priority_queue.qsize() == 0:
            return "Conversion is not possible"
        
        popped_from_queue = priority_queue.get()
        curr_LCD = popped_from_queue.get_LCD()
        before_permutations = popped_from_queue.get_new_word()
        mutate_new_word = popped_from_queue.get_new_word()

        #Run through all permutations of s1 and add them to a queue, keep track of seen words using a dictionary to account for duplicates
        for i in range(len(before_permutations)):
            if outer_bool:
                break
            mutate_new_word = before_permutations
            for j in range(97,123):
                diff_letters = 0
                char = chr(j)
                if i == 0:
                    mutate_new_word = char + mutate_new_word[1:]
                elif i == (len(before_permutations) - 1):
                    mutate_new_word = mutate_new_word[0:i] + char
                else:
                    mutate_new_word = mutate_new_word[0:i] + char + mutate_new_word[(i + 1):]
            
                if mutate_new_word == s2:
                    word_dict[mutate_new_word] = before_permutations
                    while_bool = False
                    outer_bool = True
                    break
                elif (mutate_new_word in wordset and mutate_new_word not in word_dict):
                    word_dict[mutate_new_word] = before_permutations
                    word_obj = word()
                    word_obj.set_new_word(mutate_new_word)
                    for k in range(len(s2)):
                        if mutate_new_word[k] == s2[k]:
                            diff_letters += 1
                    word_obj.set_diff_letters(diff_letters)
                    word_obj.set_LCD(curr_LCD + 1)
                    priority_queue.put(word_obj)
                    
    while (s2 != s1):
        convert_list.append(s2)
        s2 = word_dict[s2]
    
    convert_list.append(s1)
    convert_list.reverse()

    return convert_list

   

    
    
    

