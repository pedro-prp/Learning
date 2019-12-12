import Numeric
import Text.Printf

main :: IO ()
main = do
    read1 <- getLine

    let raio = read read1 :: Double
    let pi = 3.14159 :: Double
    let area = pi * (raio * raio) :: Double

    printf "%s%.4f\n" "A=" area
