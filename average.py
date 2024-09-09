"""
Import the text_utils module you created and calculate the average number of
words per line in a given text file. The text file that will be used to test
this is the text file called "sample.txt" (located in the same directory as
this exercise). The average number of words per line should be rounded down to
the nearest integer.

Print the average number of words per line in the text file in the following
format:

"Average words per line: [average]"
"""
# while the text is open....
with open("sample.txt", 'r') as file:
  # The counter is set to 0 for lines and words
  lines = 0
  words = 0
  
  for line in file.readlines():
    # adds one for every line it finds 
    lines += 1
    # splits the sentence and count how many were split up
    words += len(line.split(' '))
# print the average and rounding it down (floor)
print (f"Average words per line: {(words//lines)}")