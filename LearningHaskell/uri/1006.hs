import Text.Printf

main :: IO ()
main = do
    read1 <- getLine
    read2 <- getLine
    read3 <- getLine

    let media = ((((read read1 :: Float)*2) + ((read read2 :: Float)*3) + ((read read3 :: Float)*5))/10) :: Float

    printf "%s%.1f\n" "MEDIA = " media
