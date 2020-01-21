import Text.Printf

main :: IO ()
main = do
    read1 <- getLine
    read2 <- getLine

    let media = (((read read1 :: Double)*3.5) + ((read read2 :: Double)*7.5))/11 :: Double

    printf "%s%.5f\n" "MEDIA = " media
    