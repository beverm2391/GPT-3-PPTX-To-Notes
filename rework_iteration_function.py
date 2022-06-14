python



prompt_full = "My name is Ben"

prompt_full_chars = ""

max_chars = 3900

def getResponse(prompt):
    return f"got response for {prompt}"

# case 1: prompt_full is over the limit
# case 2: prompt full is under the limit but greater than 0

def chunkIt():
    chunk1 = "chunk"
    prompt = promptfull - chunk
    return chunk1
    

while prompt_full_chars > max_chars:

    chunkIt()
    getResponse()

    # move to next chunk

if prompt_full_chars < max_chars and prompt_full_chars> 0:

    getResponse()

def dosomething():
    return f"something {string}"

string = "This is a really long string over the word limit for the thing"
number_2 = "Short string"
limit = 20

x = 0
y = limit



while string > limit:
    slice = string[x:y]
    dosomething(slice)
    string = string[y:]

if len(string) < limit:
    dosomething(string)

