class Logfunc():
    def __init__(self ):
        self.train_loss = None 
        self.test_loss = None
        self.epoch = None
        self.correct = None
        self.total = None
        with open("log.txt", mode = "w") as f:
            f.write("start\n")
    
    def print_log(self):
        print("--------------------------------------------------------")
        print("epoch : ",self.epoch)
        print("train_loss : {:.5f}".format(self.train_loss))
        if self.test_loss:
            print("test_loss  : {:.5f}".format(self.test_loss))
        if self.correct:
            print("accuracy   : {:.1f}%".format(self.correct/self.total*100))
            print(self.correct," / ", self.total)
        
    def write_log(self):
        with open("log.txt", mode = "a") as f:
            f.write("--------------------------------------------------------\n")
            f.write("epoch : {}\n".format(self.epoch))
            f.write("train_loss : {:.5f}\n".format(self.train_loss))
            if self.test_loss:
                f.write("test_loss  : {:.5f}\n".format(self.test_loss))
            if self.correct:
                f.write("accuracy   : {:.1f}%\n".format(self.correct/self.total*100))
                f.write("{} / {}\n".format(self.correct, self.total))
    def update(self, epoch, train_loss, test_loss = None, correct = None, total = None ):
        self.train_loss = train_loss
        self.test_loss = test_loss
        self.epoch = epoch
        self.correct = correct
        self.total = total
