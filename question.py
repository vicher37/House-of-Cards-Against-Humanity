# print out the elements in a list
def show_text(qlist):
     print(qlist)
     
# define parent class Text
class Text():
    """This class defines what texts can do in this program in general. It performs functions such as adding, deleting, copying and deleting."""
    def __init__(self, text):
         self.text = text

     # print out the object
    def show_text(self):
         print(self.text)

# define child class Qst (stands for question), and define show_number function
class Qst(Text):
     """This class enables you to input questions you want to ask. You'd better have a corresponding hilarious answer in mind :)"""
     def __init__(self, text, number):
         Text.__init__(self, text)
         self.number = number

     def show_number(self):
          if self.number == 1:
               print("**This question has one blank.")
          else:
               print("**This question has two blanks.")

# define child class Ans (stands for answer), and define rate function
class Ans(Text):
     """This class enables you to input hilarious answers. """
     def __init__(self, text):
         Text.__init__(self, text)
         

     def rate(self):
          rating = input ("On a scale of 1 to 5, how would you rate the funniness of this answer? Input here ->")
          ratinglist = []
          ratinglist.append(rating)
              
          

          
