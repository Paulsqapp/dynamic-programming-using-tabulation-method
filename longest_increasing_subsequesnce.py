
sequence = [5,7,4,-3,9,1,10,4,5,8,9,3]

def lis(s): #sequence of numbers
    ''' start at the end and if the preseeding number is less than current
    The last number should be the largest
    '''
    
    index = float('-inf')
    counter = -1
    table = {}
    b = None
    
    for x in range(len(s)): #[5,7,4,-3,9,1,10,4,5,8,9,3]
        print('start', s[counter])
        item = s[counter]
        if item not in table: table[item]= [item]
        print(f'table {table}')
        for key, num in table.items():
            print('inner for',num, item)
            if item < num[-1]: 
                table[key] = num + [item]
                
                if len(table[key]) > index: 
                    index = len(table[key])
                    b = table[key]
        counter -= 1
    return b , index
y = lis(sequence)       