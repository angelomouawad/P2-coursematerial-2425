class CircularBuffer:
    def __init__(self, maxlength):
        self.maxlength = maxlength
        self.list = []

    def __len__(self):
        return len(self.list)
    
    def add(self, character):
        self.list.append(character)
        if len(self.list) > self.maxlength:
            self.list.pop(0)
        
    def __getitem__(self, index):
        return self.list[index]