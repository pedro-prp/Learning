calc x y sum cont = do
    if cont < y
        then
            calc (x+2) y (sum+x) (cont+1)
        else
            print sum

func n cont = do
    if cont < n
        then do
            a <- getLine
            let values = map read(words a) :: [Int]

            let x = values !! 0 :: Int
            let y = values !! 1 :: Int

            if x `mod` 2 == 0
                then
                    calc (x+1) y 0 0
                else
                    calc x y 0 0
            
            func n (cont+1)
        else
            return ()
            

main :: IO ()
main = do    

    n <- readLn :: IO Int

    func n 0