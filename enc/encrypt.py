allChars=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","W","Z"]


class Crypto:

    def __init__(self, step):
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
        last = allChars.index("Z")
        encrypted_text = ""
        for c in text:
            if c == " ":
                encrypted_text = encrypted_text + "&"
            elif c == "\n":
                encrypted_text = encrypted_text + "\n"
            else:
                ind = allChars.index(c)
                newInd = ind + self.step
                if newInd >= last:
                    newInd = (newInd - last)
                encrypted_text = encrypted_text + allChars[newInd]
        return encrypted_text

    def __decrypt_text(self, text):
        first = allChars.index("a")
        decrypted_text = ""
        for c in text:
            if c == "&":
                decrypted_text = decrypted_text + " "
            elif c == "\n":
                decrypted_text = decrypted_text + "\n"
            else:
                ind = allChars.index(c)
                newInd = ind - self.step
                if newInd <= first:
                    newInd = (newInd + first)
                decrypted_text = decrypted_text + allChars[newInd]
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

