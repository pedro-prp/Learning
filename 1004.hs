main :: IO ()
main = do
    a <- getLine
    b <- getLine

    putStrLn $ "PROD = " ++ show((read a :: Int) * (read b :: Int))
