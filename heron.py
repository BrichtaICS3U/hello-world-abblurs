#Heron's Method for Calculating Square Roots
#Stub by JP Brichta, March 2018
#
#Heron's method for calculating square roots is approximately 2000 years old and was devised by Hero of Alexandria. It is an
#iterative method (meaning that it uses a previous answer to calculate the next) that in principle, will continue forever.
#When using iterative method, it is important to decide if the answer is "good enough" or if the program should continue.
#You can read more about Heron's Method and other methods of computing square roots in the wikipedia entry here:
#https://en.wikipedia.org/wiki/Methods_of_computing_square_roots#Babylonian_method
#

def absolute(x):
    """Determine the absolute value of a number, x.
    """
    if x >= 0:
        return x
    else:
        return -x

def heron(x, accuracy):
  """Compute the square root of the number x using Heron's method. The accuracy is defaulted to three decimal places, but you
  can use a larger or smaller number if you wish. The smaller the number, the more time the calculation will take."""
  
  G = int(input("Enter a guess for the square root of x: "))

  while absolute((G**2)-x) >= accuracy:
      G = (G + (x/G)) / 2

  print(round(G, 3))

def newton(x, accuracy):
  G = int(input("Enter a guess for the square root of x: "))
  
  while absolute((G**2)-x) >= accuracy:
      G = G - (G**2-x) / (2*G**1)

  print(round(G,3))
  
