-- Tex

tex20 = [1 .. 20]

texAZ = ['a' .. 'z']

tex220 = [2, 4 .. 20]

tex36 = [3, 6 .. 20]

texreverse = [20, 19 .. 1]

-- Cycle
cyc123 = take 10 (cycle [1,2,3])
cycStr = take 12 (cycle "LOL ")

-- Repeat
repeat5 = take 10 (repeat 5)

-- Replicate
replicate5 = replicate 10 5

-- List comprenhension
list220 = [x*2 | x <- [1 .. 10]]
listGreater12 = [x*2 | x <- [1 .. 10], x*2 >= 12]

--      using functions
boomBang xs = [if x < 10 then "BOOM!" else "BANG!" | x <- xs, odd x]
