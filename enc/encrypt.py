class Crypto:

    def __init__(self, step):
        self.allChars=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
        self.other = ["!", "\u200b", "?", ":", ";", "/", "@", "#", "$", "%", "^", "*", "(", ")", "—", "-", "_", "+", "=", "[", "]", "{", "}", ".", ",", "'", "\""]
        self.digits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        self.step = int(step)

    def encrypt(self, text, file):
        if text is not None:
            enc_text = self.__encrypt_text(text=text)
            print(f'Encrypted text: {enc_text}')
        if file is not None:
            self.__encrypt_file(file=file)
        return 0

    def decrypt(self, text, file):
        if text is not None:
            dec_text = self.__decrypt_text(text=text)
            print(f'Decrypted text: {dec_text}')
        if file is not None:
            self.__decrypt_file(file=file)
        return 0

    def __encrypt_text(self, text):
        last = self.allChars.index("Z")
        encrypted_text = ""
        for c in text:
            if c == " ":
                encrypted_text = encrypted_text + "&"
            elif c == "\n":
                encrypted_text = encrypted_text + "\n"
            elif c in self.other:
                encrypted_text = encrypted_text + c
            elif c in self.digits:
                ind = self.digits.index(c)
                newInd = ind + self.step
                if newInd > self.digits.index("9"):
                    newInd = newInd - self.digits.index("9")
                encrypted_text = encrypted_text + self.digits[newInd]
            else:
                ind = self.allChars.index(c)
                newInd = ind + self.step
                if newInd > last:
                    newInd = (newInd - last)
                encrypted_text = encrypted_text + self.allChars[newInd]
        return encrypted_text

    def __decrypt_text(self, text):
        first = self.allChars.index("a")
        decrypted_text = ""
        for c in text:
            if c == "&":
                decrypted_text = decrypted_text + " "
            elif c == "\n":
                decrypted_text = decrypted_text + "\n"
            elif c in self.other:
                decrypted_text = decrypted_text + c
            elif c in self.digits:
                ind = self.digits.index(c)
                newInd = ind - self.step
                if newInd < self.digits.index("0"):
                    newInd = newInd + self.digits.index("0")
                decrypted_text = decrypted_text + self.digits[newInd]
            else:
                ind = self.allChars.index(c)
                newInd = ind - self.step
                if newInd < first:
                    newInd = (newInd + first -1)
                decrypted_text = decrypted_text + self.allChars[newInd]
        return decrypted_text

    def __encrypt_file(self, file):
        f = open(file, "r+")
        encr = open("output.txt", "w+")
        lines = f.readlines()
        outLines = ""
        for l in lines:
            enc = self.__encrypt_text(l)
            outLines = outLines + enc
        encr.writelines(outLines)

    def __decrypt_file(self, file):
        f = open(file, "r+")
        encr = open("output.txt", "w+")
        lines = f.readlines()
        outLines = ""
        for l in lines:
            enc = self.__decrypt_text(l)
            outLines = outLines + enc
        encr.writelines(outLines)

