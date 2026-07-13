from braillebase import BrailleBase

class BrailleBaseEnglish(BrailleBase):
    def __init__(self):

        """
        """
        super().__init__()
        self.setting_braille_rules_uppercase("⠠", "⠠⠄") #2026/05/18
        #letras min
        self.append_braille_letter("a", ["⠁"]) #2026/06/09
        self.append_braille_letter("b", ["⠃"]) #2026/06/09
        self.append_braille_letter("c", ["⠉"]) #2026/06/09
        self.append_braille_letter("d", ["⠙"]) #2026/06/09
        self.append_braille_letter("e", ["⠑"]) #2026/06/09
        self.append_braille_letter("f", ["⠋"]) #2026/06/09
        self.append_braille_letter("g", ["⠛"]) #2026/06/09
        self.append_braille_letter("h", ["⠓"]) #2026/06/09
        self.append_braille_letter("i", ["⠊"]) #2026/06/09
        self.append_braille_letter("j", ["⠚"]) #2026/06/09
        self.append_braille_letter("k", ["⠅"]) #2026/06/09
        self.append_braille_letter("l", ["⠇"]) #2026/06/09
        self.append_braille_letter("m", ["⠍"]) #2026/06/09
        self.append_braille_letter("n", ["⠝"]) #2026/06/09
        self.append_braille_letter("o", ["⠕"]) #2026/06/09
        self.append_braille_letter("p", ["⠏"]) #2026/06/09
        self.append_braille_letter("q", ["⠟"]) #2026/06/09
        self.append_braille_letter("r", ["⠗"]) #2026/06/09
        self.append_braille_letter("s", ["⠎"]) #2026/06/09
        self.append_braille_letter("t", ["⠞"]) #2026/06/09
        self.append_braille_letter("u", ["⠥"]) #2026/06/09
        self.append_braille_letter("v", ["⠧"]) #2026/06/09
        self.append_braille_letter("w", ["⠺"]) #2026/06/09
        self.append_braille_letter("x", ["⠭"]) #2026/06/09
        self.append_braille_letter("y", ["⠽"]) #2026/06/09
        self.append_braille_letter("z", ["⠵"]) #2026/06/09

       #letras maiusc
        self.append_braille_letter("A", ["⠁"],1) #2026/06/09
        self.append_braille_letter("B", ["⠃"],1) #2026/06/09
        self.append_braille_letter("C", ["⠉"],1) #2026/06/09
        self.append_braille_letter("D", ["⠙"],1) #2026/06/09
        self.append_braille_letter("E", ["⠑"],1) #2026/06/09
        self.append_braille_letter("F", ["⠋"],1) #2026/06/09
        self.append_braille_letter("G", ["⠛"],1) #2026/06/09
        self.append_braille_letter("H", ["⠓"],1) #2026/06/09
        self.append_braille_letter("I", ["⠊"],1) #2026/06/09
        self.append_braille_letter("J", ["⠚"],1) #2026/06/09
        self.append_braille_letter("K", ["⠅"],1) #2026/06/09
        self.append_braille_letter("L", ["⠇"],1) #2026/06/09
        self.append_braille_letter("M", ["⠍"],1) #2026/06/09
        self.append_braille_letter("N", ["⠝"],1) #2026/06/09
        self.append_braille_letter("O", ["⠕"],1) #2026/06/09
        self.append_braille_letter("P", ["⠏"],1) #2026/06/09
        self.append_braille_letter("Q", ["⠟"],1) #2026/06/09
        self.append_braille_letter("R", ["⠗"],1) #2026/06/09
        self.append_braille_letter("S", ["⠎"],1) #2026/06/09
        self.append_braille_letter("T", ["⠞"],1) #2026/06/09
        self.append_braille_letter("U", ["⠥"],1) #2026/06/09
        self.append_braille_letter("V", ["⠧"],1) #2026/06/09
        self.append_braille_letter("W", ["⠺"],1) #2026/06/09
        self.append_braille_letter("X", ["⠭"],1) #2026/06/09
        self.append_braille_letter("Y", ["⠽"],1) #2026/06/09
        self.append_braille_letter("Z", ["⠵"],1) #2026/06/09

        #number
        self.append_braille_letter("⠼", ["⠼"]) #2026/06/09
        self.append_braille_letter("1", ["⠁"]) #2026/06/09
        self.append_braille_letter("2", ["⠃"]) #2026/06/09
        self.append_braille_letter("3", ["⠉"]) #2026/06/09
        self.append_braille_letter("4", ["⠙"]) #2026/06/09
        self.append_braille_letter("5", ["⠑"]) #2026/06/09
        self.append_braille_letter("6", ["⠋"]) #2026/06/09
        self.append_braille_letter("7", ["⠛"]) #2026/06/09
        self.append_braille_letter("8", ["⠓"]) #2026/06/09
        self.append_braille_letter("9", ["⠊"]) #2026/06/09
        self.append_braille_letter("0", ["⠚"]) #2026/06/09
        
        self.append_braille_letter(".", ["⠲"]) #2026/06/09
        self.append_braille_letter(",", ["⠂"]) #2026/06/09
        self.append_braille_letter(";", ["⠆"]) #2026/06/09
        self.append_braille_letter(":", ["⠒"]) #2026/06/09
        self.append_braille_letter("!", ["⠖"]) #2026/06/09
        self.append_braille_letter("?", ["⠦"]) #2026/06/09
        self.append_braille_letter("\u0027", ["⠄"]) #2026/06/09 '
        self.append_braille_letter("\u0022", ["⠄", "⠶"]) #2026/06/09 "
        

        self.append_braille_letter("“", ["⠘", "⠦"]) #2026/06/09
        self.append_braille_letter("”", ["⠘", "⠴"]) #2026/06/09
        self.append_braille_letter("‘", ["⠄", "⠦"]) #2026/06/09
        self.append_braille_letter("’", ["⠄", "⠴"]) #2026/06/09
        self.append_braille_letter("(", ["⠐", "⠣"]) #2026/06/09
        self.append_braille_letter(")", ["⠐", "⠜"]) #2026/06/09
        self.append_braille_letter("\u002F", ["⠸", "⠌"]) #2026/06/09 /
        self.append_braille_letter("\u005C", ["⠸", "⠡"]) #2026/06/09 \


        #math
        self.append_braille_letter("\u0023", ["⠸", "⠹"]) #2026/06/09 #
        self.append_braille_letter("+", ["⠐", "⠖"]) #2026/06/09
        self.append_braille_letter("−", ["⠐", "⠤"]) #2026/06/09
        self.append_braille_letter("×", ["⠐", "⠦"]) #2026/06/09
        self.append_braille_letter("*", ["⠐", "⠔"]) #2026/06/09
        self.append_braille_letter("÷", ["⠐", "⠌"]) #2026/06/09
        self.append_braille_letter("%", ["⠨", "⠴"]) #2026/06/09
        self.append_braille_letter("=", ["⠐", "⠶"]) #2026/06/09


        #money simbol
        self.append_braille_letter("$", ["⠈", "⠎"]) #2026/06/09
        self.append_braille_letter("¢", ["⠈", "⠉"]) #2026/06/09
        self.append_braille_letter("¥", ["⠈", "⠽"]) #2026/06/09
        self.append_braille_letter("€", ["⠈", "⠑"]) #2026/06/09
        self.append_braille_letter("£", ["⠈", "⠇"]) #2026/06/09
        self.append_braille_letter("₣", ["⠈", "⠋"]) #2026/06/09
        self.append_braille_letter("₦", ["⠈", "⠝"]) #2026/06/09

        #yajiru
        self.append_braille_letter("→", ["⠳", "⠕"]) #2026/06/09
        self.append_braille_letter("↓", ["⠳", "⠩"]) #2026/06/09
        self.append_braille_letter("←", ["⠳", "⠪"]) #2026/06/09
        self.append_braille_letter("↑", ["⠳", "⠬"]) #2026/06/09

        #general
        self.append_braille_letter("©", ["⠘", "⠉"]) #2026/06/09
        self.append_braille_letter("®", ["⠘", "⠗"]) #2026/06/09
        self.append_braille_letter("™", ["⠘", "⠞"]) #2026/06/09
        self.append_braille_letter("♀", ["⠘", "⠭"]) #2026/06/09
        self.append_braille_letter("♂", ["⠘", "⠽"]) #2026/06/09
        self.append_braille_letter("§", ["⠘", "⠎"]) #2026/06/09

        #internet
        self.append_braille_letter("@", ["⠈", "⠁"]) #2026/06/09

