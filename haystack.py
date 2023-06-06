def findNeedle(haystack, needle): 
    print ("We are checking this haystack " + haystack + "for this needle " + needle)
    start_index = -1
    H_index_counter = 0
    N_index_counter = 0
    for Hletter in haystack: 
        for Nletter in needle: 
            print("About to check the following Hletter, Nletter pair: " + Hletter + Nletter + ". The indices are "+ str(H_index_counter) + str(N_index_counter))
            if Nletter == Hletter: 
                print("Hletter and Nletter match, they are " + Hletter + Nletter + "found at indexes for H and N " + str(H_index_counter) + str(N_index_counter))
                if N_index_counter == 0:
                    print("We have entered the match case, and it is potentially beginning of haystack. The Needle, Haystack letter combo is " + str(Nletter) + str(Hletter))
                    start_index = H_index_counter
                elif N_index_counter == len(needle) - 1:
                    print("This means we should have found the needle")
                    print("Should be returning " + str(start_index))
                    return start_index
                H_index_counter += 1
                if H_index_counter < len(haystack):    
                    Hletter = haystack[H_index_counter]
            else:
                start_index = -1
                print("We know it is not the beginning of Needle. The haystack needle pair is " + Hletter + Nletter)
                break
            N_index_counter += 1 
        N_index_counter = 0        
        H_index_counter += 1       
    return -1 