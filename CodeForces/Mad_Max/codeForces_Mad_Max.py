import sys
input = sys.stdin.readline

############ ---- Input Function ---- ############

def inlt():
    return(list(map(int,input().split())))



############ ---- Algo ---- ############
# Maximizing the dog food

def max_dog_food(n, m, f, hitchhikers_list):
    dog_food = 0
    fuel = f
    c = [[0 for x in range(m+1)] for y in range(n+1)]
    for i in range(n):
        for j in range(m):
            if i == 0 or j == 0:
                c[i][j] = 0
            elif (fuel > 0) and (fuel + hitchhikers_list[j][3] -
                    (hitchhikers_list[j][1] - i) >= 0):
                c[i][j] = max(hitchhikers_list[j][2] + c[hitchhikers_list[j][1]][j], c[i-1][j])
            elif (fuel == 0 and (fuel + hitchhikers_list[j][3] -
                    (hitchhikers_list[1] - i) < 0)):
                return -1
            else:
                c[i][j] = c[i-1][j]
    for i in range(n+1):
        print(c[i])
    return c[n][m]

    #print matrix c



def max_dog_food_top_down(n, m, f, hitchhikers_list):
    r = [0 for x in range(n+1)]
    r[0] = 0
    for i in range(1, n+1):
        r[i] = -1000
    #d = 0
    return max_dog_food_top_down_aux(1, n, m, f, hitchhikers_list, r)#, d)


def max_dog_food_top_down_aux(start, n, m, f, hitchhikers_list, r):#, d):
    print("BEGIN DEF")
    print("r : {}".format(r))
    print()

    if(r[n] >= 0):
        return r[n]
    else:
        dog_food = 0 #aaaaa
        for i in range(start, n+1):
            #list_hiker_post_i = []
            print("GUS AU POST {}".format(i))
            for j in range(0, m):
                if(hitchhikers_list[j][0] == i):
                    print(hitchhikers_list[j])
                    #list_hiker_post_i.append(hitchhikers_list[j][1])
                    fuel_if_take_it = f + hitchhikers_list[j][3] - (hitchhikers_list[j][1] - i)
                    if((f >= 0) and (fuel_if_take_it >= 0)):
                        dog_food = max(dog_food, hitchhikers_list[j][2] + max_dog_food_top_down_aux(hitchhikers_list[j][1], n, m, fuel_if_take_it ,hitchhikers_list, r))
            print()
            f -= 1
        r[start] = dog_food

    return r[start]

                #if(f > 0 and (fuel + hitchhikers_list[j][3] - (hitchhikers_list[j][1] - i) >= 0))
                #r[i] = max(hitchhikers_list[i][2] + c[hitchhikers_list[i][1]][j], c[i-1][j])








############ ---- Read Input ---- ############

#firstLine = inlt()

#n = firstLine[0] # Number of post
#m = firstLine[1] # Number of hitchhikers
#f = firstLine[2] # Initial liter of gasoline

#hitchhikers_list = [] # List of [post number, dest, dog food, gasoline]

#for i in range(m):
#    hitchhikers_i = inlt()
#    hitchhikers_list.append(hitchhikers_i)


#ex: food must be 15
n_t = 10
m_t = 9
f_t = 2
hitchhikers_list_t = [[1,3,3,1], [2,4,2,2], [3,5,3,3], [4,6,2,1], [6,8,1,3],
                      [7,8,2,1], [8,10,5,2], [8,9,1,1], [9,10,5,1]]

print(max_dog_food_top_down(3, 3, 1, [[1, 3, 1, 2], [1, 3, 5, 0],[2, 3, 4 ,1]]))
#print(max_dog_food_top_down(3, 1, 1, [[2, 3, 3, 0]]))

#print(max_dog_food_top_down(n_t, m_t, f_t, hitchhikers_list_t))
