import haystack as hs

def main (): 
    tests = []
    tests.append(("miss", "iss", "result should be 1"))
    tests.append(("shacker", "acke", "result should be 2"))
    tests.append(("stand", "nope", "result should be -1"))
    tests.append(("100", "00", "results should be 1"))
    tests.append(("Mississippi", "issip", "results should be 1"))
    tests.append(("Mississippi", "sis", "results should be 3"))
    tests.append(("Mississippi", "issip", "results should be 4"))
    tests.append(("Mississippi", "sip", "results should be 6"))
    tests.append(("Mississippi", "ippi", "results should be 7"))
    for test in tests: 
        print (str(hs.findNeedle(test[0], test[1])) + test[2])
    # print (hs.findNeedle())

main()