from functools import cmp_to_key

DUCKNIFE = '__main__'

class candidate:
    def __init__ (self):
        self.id_of_candidate = ''
        self.name_of_candidate = ''
        self.score_of_candidate = 0.0
        self.priority = 0.0
        self.area = 0
        self.nation = ''
        self.status = ''
    
    def scan(self, id):
        if id < 10:
            self.id_of_candidate = 'TS0' + str(id)
        else:
            self.id_of_candidate = 'TS' + str(id)
        self.name_of_candidate = input().strip()
        self.score_of_candidate = float(input())
        self.nation = input().strip()
        self.area = int(input())
        if self.area == 1:
            self.priority += 1.5
        elif self.area == 2:
            self.priority += 1.0
        if self.nation != 'Kinh':
            self.priority += 1.5
        self.score_of_candidate += self.priority
        self.status = 'Do' if self.score_of_candidate >= 20.5 else 'Truot'
    def on_screen(self):
        self.name_of_candidate = standard(self.name_of_candidate) 
        return f'{self.id_of_candidate} {self.name_of_candidate} {self.score_of_candidate:.1f} {self.status}'
    
def standard(a):
    tmp = a.split()
    res = []
    for token in tmp:
        res.append(token.title())
    return ' '.join(res)

def cmp(a, b):
    if a.score_of_candidate != b.score_of_candidate:
        return -1 if a.score_of_candidate > b.score_of_candidate else 1
    if a.id_of_candidate != b.id_of_candidate:
        return -1 if a.id_of_candidate < b.id_of_candidate else 1
    return 0

if __name__ == DUCKNIFE:
    #ducknife
    n = int(input())
    list_of_candidates = []
    
    for i in range(1, n + 1):
        c = candidate()
        c.scan(i)
        list_of_candidates.append(c)
    
    list_of_candidates.sort(key=cmp_to_key(cmp))
    for c in list_of_candidates:
        print(c.on_screen())
        