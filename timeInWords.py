#timeInWords.py


def timeInWords(h, m):
    result =''
    
    nums = ["zero", "one", "two", "three", "four", 
                "five", "six", "seven", "eight", "nine", 
                "ten", "eleven", "twelve", "thirteen", 
                "fourteen", "fifteen", "sixteen", "seventeen", 
                "eighteen", "nineteen", "twenty", "twenty one", 
                "twenty two", "twenty three", "twenty four", 
                "twenty five", "twenty six", "twenty seven", 
                "twenty eight", "twenty nine"]
                      
  
    if (m == 0):
        result = "{} o' clock\n".format(nums[h])
    elif m == 1:
        result = "one minute past {}\n".format(nums[h])
    elif m == 59:
        result = "one minute to {}\n".format(nums[(h % 12) + 1])
    elif m == 15:
       result = "quarter past {}\n".format(nums[h])
    elif m == 30:
        result = "half past {}\n".format(nums[h])
    elif m == 45:
        result = "quarter to {}\n".format(nums[(h % 12) + 1]) 
    elif m <= 30:
        result = "{} minutes past {}\n".format(nums[m], nums[h]) 
    elif m > 30: 
        result = "{} minutes to {}\n".format(nums[60 - m],nums[(h % 12) + 1])
    return result


h = 1
m = 1
print(timeInWords(h, m))
