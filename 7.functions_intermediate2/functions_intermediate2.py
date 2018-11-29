x = [ [5,2,3], [10,8,9] ] 
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

x[1][0] = 15
students[0]['last_name'] = 'Bryant'
sports_directory['soccer'][0] = 'Andres'
z[0]['y'] = 30



def iterateDictionary(dict_list):
    for i in dict_list:
        for key, val in i.items():
            print(key, '-', val)



def iterateDictionary2(key, dict_list):
    for i in dict_list:
        for key, val in i.items():
            if key == 'first_name':
                print(val)



def printDojoInfo(dict):
    print(len(dict['locations']), 'LOCATIONS')
    for val in dict['locations']:
        print(val)
    print("")
    print(len(dict['instructors']), 'INSTRUCTORS')
    for val in dict['instructors']:
        print(val)