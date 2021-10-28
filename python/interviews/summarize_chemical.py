
# Write a function that accepts a string representation of a chemical compound and returns a JSON object containing KV pairs where keys are the element symbols and the values are the element counts.

# "H2O" => {"H": 2, "O": 1}
# "C6H12" => {"C": 6, "H": 12}
# "COOH" => {"C": 1, "O": 2, "H": 1}

# @netskope.com

def summarize_chemical(input: str) -> dict:
    output = dict()
    
    def is_int(b: str) -> bool:
        try:
            int(b)
        except:
            return False
        return True
        
    idx = 0    
    while idx < len(input):
            # print(idx, input[idx])
            if not is_int(input[idx]):
                output.setdefault(input[idx], 0)
                # check if the next is int or not
                if idx+1 < len(input) and is_int(input[idx+1]):
                    # next exist and is a int
                    ori_idx = idx
    
                    idx += 1
                    sum = int(input[idx])
                    # loop only if the next of the next is int
                    while idx + 1 < len(input) and is_int(input[idx+1]):
                        sum = sum * 10 + int(input[idx+1])
                        # forward the index if it's after processing the int
                        idx += 1

                    output[input[ori_idx]] += sum
                else:
                    # next don't exist or it's not a int, go ahead and add 1
                    output[input[idx]] += 1
                idx += 1
                
    return output

ret = summarize_chemical("C6H12")
print(f"ret01: {ret}")

ret = summarize_chemical("H2O")
print(f"ret02: {ret}")

ret = summarize_chemical("COOH")
print(f"ret03: {ret}")