-- simple list
numbers = [4,8,15,16,23,42]


-- concact two lists
sum_list = [1,2,3] ++ [4,5,6]


-- strings are a char list
woot = ['w','o'] ++ ['o', 't']

hello = "Hello" ++ " " ++ "World"


-- append

--      in the start
numbers_append_start = 99 : numbers


-- String appends
--      a char
str_append = 'A':" SMALL PLACE"


-- Get index
pos_6_str = str_append !! 6
pos_0_numbers = numbers_append_start !! 0


-- list functions
l_head = head [5, 4, 3, 2, 1]
l_last = last [5, 4, 3, 2, 1]

l_tail = tail [5, 4, 3, 2, 1]
l_init = init [5, 4, 3, 2, 1]

l_length = length [5, 4, 3, 2, 1]
l_null = null []
l_reverse = reverse [5, 4, 3, 2, 1]

l_take_3 = take 3 [5, 4, 3, 2, 1]
-- result: [5,4,3]
l_take_1 = take 1 [5, 4, 3, 2, 1]
-- result: [5]

l_drop = drop 3 [5, 4, 3, 2, 1]
-- result: [2,1]

l_minimum = minimum [5, 4, 3, 2, 1]
l_maximum = maximum[5, 4, 3, 2, 1]

l_sum = sum [5,2,1,6,3,2,5,7]  
l_product = product [6,2,1,2]

4_in =  4 `elem` [3,4,5,6]  
-- True  
10_in = 10 `elem` [3,4,5,6]  
-- False
