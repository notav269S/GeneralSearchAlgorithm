def advanced_search(keywords, inlist):
    matches = {}
    for _ in inlist:
        matches[_] = 0
    for line in inslist:
        for letter in line:
            for _letter in keywords:
                if letter == _letter:
                    matches[name] += 1
    try:
        del(matches['\n'])
    except:
        pass
      
    max_key = max(matches, key=matches.get)
    return max_key
  
def simple_search(keywords, inlist):
    if keywords in inlist:
        return keywords
     else:
        return None
