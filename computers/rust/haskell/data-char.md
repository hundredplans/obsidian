Exports functions that deal with characters

# Predicates
All the functions below have a signature of Char -> Bool
    isControl -> Return true if char is a control character
    isSpace -> Return true if char is a white-space character
    isLower
    isUpper
    isAlpha -> Return true if char is an english letter
    isAlphaNum -> Return true if isAlpha or num
    isPrint -> Return true if character is printable (not Control characters)
    isDigit -> Return true if character is 0-9
    isOctDigit
    isHexDigit
    isLetter -> Return true if char is a letter according to Unicode
    isMark -> Return true if unicode mark characters
    isNumber -> Return true if character is a number (from any language)
    isPunctuation
    isSymbol -> Return true if it's a mathematical or currency symbol
    isSeperator -> Return true if it's a unicode space or seperator
    isAscii -> Return true if character is in first 128 characters of Unicode
    isAsciiUpper
    isAsciiLower
    isLatin1 -> Return true if character is in first 256 characters of Unicode

GeneralCategory type
generalCategory 'A' -> UppercaseLetter (compares using generalCategory type)
generalCategory c == Space (generalCategory is part of the Eq typeclass)

# Conversion Functions
toUpper char
toLower char
toTitle char -> Converts to title-case (same as upper-case for most characters)
digitToInt char -> Char must be in range 0-9, a-f, A-F
intToDigit num -> Num must be in range 0-9
ord char -> Converts to Unicode number
chr num -> Converts num to Unicode character
