class Question():
    def __init__(self , text , true , false1 , false2 , false3):
        self.text = text
        self.true = true
        self.false1 = false1
        self.false2 = false2
        self.false3 = false3
        questions.append(self)
    
    def show_question(self, lb, rb1, rb2, rb3, rb4):
        lb.setText(self.text)
        rb1.setText(self.true)
        rb2.setText(self.false1)
        rb3.setText(self.false2)
        rb4.setText(self.false3)

questions = []

Question("3 + 2 = ", "5", "6", "2", "0")        
Question("5 + 6 = ", "11", "12", "10", "56")
Question("9 + 7 = ", "16", "97", "79", "15")
Question("5 * 5 = ", "25", "35", "10", "15")
Question("9 * 7 = ", "63", "16", "2", "62")
Question("12 * 13 = ", "156", "165", "155", "145")
Question("2^2^2^2 = ", "256", "128", "16", "8")
Question("2^(64/32) = ", "4", "8", "2", "10")
Question("3 * (3 ^ 3) = ", "81", "80", "27", "91")
Question("4*4-4+(2^3) = ", "20", "30", "16", "4")
