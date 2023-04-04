B = 128
Q = 37

def read_input():
    txt=input()
    if "F" in txt:
        filename=input()
        if "a" not in filename:
            with open(str("test/"+filename), mode="r") as fails:
                pattern = fails.readline()
                text = fails.readline()
            return (pattern.rstrip(), text.rstrip())
        else:
            print("error")
    elif "I" in txt:
        return (input().rstrip(), input().rstrip())
    else:
        print("Input error")

def print_occurrences(output):
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    # this function should find the occurances using Rabin Karp alghoritm 
    # and return an iterable variable
    occurrences = []
    pat_len = len(pattern)
    text_len = len(text)
    pat_hash = get_hash(pattern)
    mtext = get_hash(text[:pat_len])
    mult = 1
    for i in range(1, pat_len):
        mult = (mult * B) % Q
    
    for i in range(text_len - pat_len + 1):
        if i != 0:
            # calculate next substring hash
            mtext = ((mtext - ord(text[i - 1]) * mult) * B + ord(text[i + pat_len - 1])) % Q
        if pat_hash == mtext:
            if pattern == text[i:(i + pat_len)]:
                occurrences.append(i)       
    # and return an iterable variable
    return occurrences

def get_hash(pattern: str) -> int:
    m = len(pattern)
    result=0
    for i in range(m):
        result = (B * result + ord(pattern[i])) % Q
    return result


if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))