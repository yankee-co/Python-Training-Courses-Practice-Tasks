class Vocabulary:
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
        s = ''
        t = tuple()
        for i in self.words.keys():
            for v in self.words[i]:
                s += v + ' '
            t += (s, )
            s = ''
        return t

    def __len__(self):
        return len(self.words)

    def __delitem__(self, key):
        return self.words.pop(key)

    def __str__(self):
        s = ''
        show = ''
        for i in self.words.keys():
            l = [*self.words[i]]
            for v in l:
                s += v + ' '
            show += '{} => {}'.format(i, s) + '\n'
            s = ''
        return show

    def contains(self, word):
        keys = [*self.words.keys()]
        if word.capitalize() in keys: return True
        for i in keys:
            if word.capitalize() in [v for v in self.words[i]]: return True
        return False

    def count(self, word = None):
        count = 0
        if word == None:
            s = []
            for i in self.words.keys():
                for v in self.words[i]: s.append(v)
            for i in s:
                count+=1
            for i in self.words.keys():
                count+=1
            return count
        if word != None:
            word = word.capitalize()
            for i in self.words[word]:
                count+=1
            return count

    def empty(self):
        if self.words == {}: return True
        return False
