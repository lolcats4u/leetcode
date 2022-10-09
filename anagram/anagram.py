class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        import string
        
        def make_dict(word: str) -> dict:
            alphabet = list(string.ascii_lowercase)
            start_count = 0
            alpha_dict = dict.fromkeys(alphabet, start_count)
            
            word_list = list(word)
            
            for letter in alpha_dict:
                alpha_dict[letter] = word_list.count(letter)

            return alpha_dict
        
        def is_anagram(s_dict: dict, t_dict: dict) -> bool:
            for i,j in zip(s_dict.values(), t_dict.values()):
                if i != j:
                    return False
                
            return True

        return is_anagram(make_dict(s), make_dict(t))