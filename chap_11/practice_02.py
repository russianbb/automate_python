# 2. Write an assert statement that triggers an AssertionError if the variables
#    eggs and bacon contain strings that are the same as each other, even if
#    their cases are different (that is, 'hello' and 'hello' are considered the
#    same, and 'goodbye' and 'GOODbye' are also considered the same).

eggs = 'helloaa'
bacon = 'Hello'

assert eggs.lower() != bacon.lower(), 'Eggs and Bacon can`t be the same.'