class FileReader:
    def __init__(self, filename):
        self.file = filename
        self.observers = []

    def subscribe(self, *observer):
        for i in observer:
            self.observers.append(i)

    def read(self):
        with open(self.file, encoding='utf-8') as file:
            for line in file:
                line = line.strip()
                for observer in self.observers:
                    observer.onReceive(line)
class Observer:
    def onReceive(self, line):
        raise NotImplementedError('define onRecieve')

class PrintObserver(Observer):
    def onReceive(self, line: str):
        print(line)

class WordCountObserver(Observer):
    def __init__(self):
        self.counter = 0
    def onReceive(self, line: str):
        self.counter += (len(line.split()))

    def printResult(self):
        print(self.counter)

class KeyWordSearchObserver(Observer):
    def __init__(self, keyword: str):
        self.keyword = keyword
        self.found = False
    def onReceive(self, line: str):
        if self.keyword.lower() in line.lower():
            self.found = True

    def printResult(self):
        print(self.found)


if __name__ == '__main__':
    reader = FileReader('test.txt')
    printer = PrintObserver()
    wordcounter = WordCountObserver()
    searcher = KeyWordSearchObserver('щука')
    reader.subscribe(printer, wordcounter, searcher)
    reader.read()
    wordcounter.printResult()
    searcher.printResult()
