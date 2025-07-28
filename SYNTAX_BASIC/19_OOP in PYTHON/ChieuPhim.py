from functools import cmp_to_key

DUCKNIFE = '__main__'

film_types = {}

class film:
    def __init__(self):
        self.id_of_film = ''
        self.type_of_film_key = ''
        self.type_of_film_value = ''
        self.name_of_film = ''
        self.full_date = ''
        self.date, self.month, self.year, self.episode = 0, 0, 0, 0
        
    def scan(self, id):
        if id < 10:
            self.id_of_film = 'P00' + str(id)
        elif id < 100:
            self.id_of_film = 'P0' + str(id)
        else:
            self.id_of_film = 'P' + str(id)
        self.type_of_film_key = input().strip()
        self.type_of_film_value = film_types[self.type_of_film_key]
        self.full_date = input().strip()
        self.date, self.month, self.year = map(int, self.full_date.split('/'))
        self.name_of_film = input().strip() 
        self.episode = int(input())
        
    def on_screen(self):
        return f'{self.id_of_film} {self.type_of_film_value} {self.full_date} {self.name_of_film} {self.episode}'   

def cmp(a, b):
    if a.year != b.year:
        return -1 if a.year < b.year else 1
    if a.month != b.month:
        return -1 if a.month < b.month else 1
    if a.date != b.date:
        return -1 if a.date < b.date else 1
    if a.name_of_film != b.name_of_film:
        return -1 if a.name_of_film < b.name_of_film else 1
    if a.episode != b.episode:
        return -1 if a.episode > b.episode else 1
    return 0
    
if __name__ == DUCKNIFE:
    #ducknife
    types, films = map(int, input().split())
    cnt_t, cnt_f = 0, 0
    list_of_films = []
    
    while cnt_t < types:
        ft = input().strip()
        if ft:
            cnt_t += 1
            t = ''
            if cnt_t < 10:
                t = 'TL00' + str(cnt_t)
            elif cnt_t < 100:
                t = 'TL0' + str(cnt_t)
            else:
                t = 'TL' + str(cnt_t)
            film_types[t] = ft
            
    while cnt_f < films:
        f = film()
        cnt_f += 1
        f.scan(cnt_f)
        list_of_films.append(f)
        
    list_of_films.sort(key=cmp_to_key(cmp)) 
    for f in list_of_films:
        print(f.on_screen())
    
        
        
        
    