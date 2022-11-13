def advanced_search(keywords, inlist):
    matches = {}
    for _ in inlist:
        matches[_] = 0
    for line in inlist:
        for letter in line.lower():
            for _letter in keywords.lower():
                if letter == _letter:
                    matches[line] += 1
    try:
        del(matches['\n'])
    except:
        pass
      
    max_key = max(matches, key=matches.get)
    return max_key
  
def simple_search(keywords, inlist):
    for letter in inlist:
        if keywords.lower() in letter.lower():
            return keywords
        else:
            return None
