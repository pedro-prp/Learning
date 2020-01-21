main :: IO ()
main = do
    read1 <- getLine
    read2 <- getLine

    let a = read read1 :: Int
    let b = read read2 :: Int

    putStrLn $ "SOMA = " ++ show(a+b)
