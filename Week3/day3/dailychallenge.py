




class Pagination :
    def __init__(self, items=None, pageSize =10, currentPage= 0):
        self.items = items
        self.pageSize = pageSize
        self.currentPage = 1
    
    def getVisibleItems(self):
        if self.pageSize <= 10:
            return self.items[:self.pageSize]
        else:
            print("You dont have enough space")

    def firstPage(self):
        return self.items[0:self.pageSize]

    def nextPage(self):
        if self.currentPage < self.getNumPages():
            self.currentPage += 1
        # current_page = len(self.getVisibleItems())
        # nextpage = self.items[current_page:current_page+self.pageSize]
        # return nextpage

    def prevPage(self):
        if self.currentPage > 1:
            self.currentPage -= 1
        

    def lastPage(self):
         self.currentPage = self.getNumPages()

    def getNumPages(self):
        return (len(self.items) + self.pageSize - 1) // self.pageSize


alphabetList = list("abcdefghijklmnopqrstuvwxyz")

p = Pagination(alphabetList, 4)
# print(p)

# print (p.getVisibleItems())
# ["a", "b", "c", "d"]
p.firstPage()
print(p.firstPage())
print(p.nextPage())
print(p.lastPage()) 

