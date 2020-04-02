#workbook.py

def workbook(n,k,a):
    '''Return count of "result" -> same problem number as page number.

    n: total chapters
    k: max problems per page
    a[i] total problems in chapter i+1 '''

    result = 0
    cur_page=1

    for i in range(len(a)):

        num_probs_in_chapter=a[i]
        num_full_pages, leftover_probs = divmod(num_probs_in_chapter, k)

        total_pages = num_full_pages + ( 1 if leftover_probs else 0 )
        problems_in_chapter=iter(range(1, a[i]+1))

        for _ in range(total_pages):
            probs_on_page = [next(problems_in_chapter, None) for _ in range(k)]    
            if cur_page in probs_on_page:

                result +=1
            cur_page+=1        
    return result


n = 15
k = 20
a = [1,8,19,15,2,29,3,2,25,2,19,26,17,33,22]
print (workbook(n, k, a))

