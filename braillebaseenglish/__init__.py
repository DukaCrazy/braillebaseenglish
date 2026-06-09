from braillebase import BrailleBase

class BrailleBaseEnglish(BrailleBase):
    def __init__(self):

        """
        """
        super().__init__()
        self.setting_braille_rules01("⠠", "⠠⠄") #2026/05/18
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
        self.append_special_braille_lettr_rules01("A", ["⠁"]) #2026/06/09
        self.append_special_braille_lettr_rules01("B", ["⠃"]) #2026/06/09
        self.append_special_braille_lettr_rules01("C", ["⠉"]) #2026/06/09
        self.append_special_braille_lettr_rules01("D", ["⠙"]) #2026/06/09
        self.append_special_braille_lettr_rules01("E", ["⠑"]) #2026/06/09
        self.append_special_braille_lettr_rules01("F", ["⠋"]) #2026/06/09
        self.append_special_braille_lettr_rules01("G", ["⠛"]) #2026/06/09
        self.append_special_braille_lettr_rules01("H", ["⠓"]) #2026/06/09
        self.append_special_braille_lettr_rules01("I", ["⠊"]) #2026/06/09
        self.append_special_braille_lettr_rules01("J", ["⠚"]) #2026/06/09
        self.append_special_braille_lettr_rules01("K", ["⠅"]) #2026/06/09
        self.append_special_braille_lettr_rules01("L", ["⠇"]) #2026/06/09
        self.append_special_braille_lettr_rules01("M", ["⠍"]) #2026/06/09
        self.append_special_braille_lettr_rules01("N", ["⠝"]) #2026/06/09
        self.append_special_braille_lettr_rules01("O", ["⠕"]) #2026/06/09
        self.append_special_braille_lettr_rules01("P", ["⠏"]) #2026/06/09
        self.append_special_braille_lettr_rules01("Q", ["⠟"]) #2026/06/09
        self.append_special_braille_lettr_rules01("R", ["⠗"]) #2026/06/09
        self.append_special_braille_lettr_rules01("S", ["⠎"]) #2026/06/09
        self.append_special_braille_lettr_rules01("T", ["⠞"]) #2026/06/09
        self.append_special_braille_lettr_rules01("U", ["⠥"]) #2026/06/09
        self.append_special_braille_lettr_rules01("V", ["⠧"]) #2026/06/09
        self.append_special_braille_lettr_rules01("W", ["⠺"]) #2026/06/09
        self.append_special_braille_lettr_rules01("X", ["⠭"]) #2026/06/09
        self.append_special_braille_lettr_rules01("Y", ["⠽"]) #2026/06/09
        self.append_special_braille_lettr_rules01("Z", ["⠵"]) #2026/06/09

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

#bb = BrailleBaseEnglish()
#print(bb.translate_text_to_braille("i like play game. I'm DOGger"))