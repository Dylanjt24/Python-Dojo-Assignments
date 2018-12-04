class Underscore:
    def map(self, list, func):
        for i in range(len(list)):
            list[i] = func(list[i])
        return list
        
    def find(self, list, func):
        for i in range(len(list)):
            if func(list[i]):
                return list[i]
    
    def filter(self, list, func):
        new_list = []
        for i in range(len(list)):
            if func(list[i]):
                new_list.append(list[i])
        return new_list
    
    def reject(self, list, func):
        new_list = []
        for i in range(len(list)):
            if not func(list[i]):
                new_list.append(list[i])
        return new_list

_ = Underscore()