""" Vocabulary module """

class Vocabulary:

    """ Vocabulary of english words and their translations """

    words: dict = {}

    def __setitem__(self, key, value):
        key = key.capitalize()
        value = value.capitalize()
        tupled = (value,)
        if key not in self.words.keys():
            self.words.update({key:tupled})
        else:
            self.words[key] += (value,)
        return self.words

    def __getitem__(self, word):
        string = ''
        tup = tuple()
        for ind in self.words:
            for value in self.words[ind]:
                string += value + ' '
            tup += (string, )
            string = ''
        return tup

    def __len__(self):
        return len(self.words)

    def __delitem__(self, key):
        return self.words.pop(key)

    def __str__(self):
        string = ''
        show = ''
        for ind in self.words:
            slist = [*self.words[ind]]
            for value in slist:
                string += value + ' '
            show += '{} => {}'.format(ind, string) + '\n'
            string = ''
        return show

    def contains(self, word):
        """ If the word is in the vocabulary or not """
        keys = [*self.words.keys()]
        if word.capitalize() in keys:
            return True
        for i in keys:
            if word.capitalize() in self.words[i]:
                return True
        return False

    def count(self, word):
        """ How many of translations word has """
        count = 0
        if word is None:
            string = []
            for ind in self.words:
                for value in self.words[ind]:
                    string.append(value)
            for ind in string:
                count+=1
            return count
        if word is not None:
            word = word.capitalize()
            for ind in self.words[word]:
                count+=1
            return count
        return None

    def empty(self):
        """ Is vocabulary empty or not """
        if self.words == {}:
            return True
        return False
