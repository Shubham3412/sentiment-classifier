file = open("project_twitter_data.csv", 'r')
lines = file.readlines()
punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
# lists of words to use
positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())

negative_words = []
with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())


def strip_punctuation(x):
    p = ""
    for y in x:
        if y not in punctuation_chars:
            p = p + y
    return p


def get_pos(r):
    num = 0
    for z in r.split():
        if z in positive_words:
            num = num + r.count(z)
    return num


def get_neg(r):
    num = 0
    for z in r.split():
        if z in negative_words:
            num = num + r.count(z)
    return num


outfile = open("resulting_data.csv", 'w')
outfile.write('Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score')
outfile.write('\n')
for line in lines[1:]:
    line = line.split(',')
    r = strip_punctuation(line[0].lower())
    y = get_pos(r)
    s = get_neg(r)
    d = y - s
    row_string = ','.join([line[1], line[2].replace("\n", ""), str(y), str(s), str(d)])
    # row_string="{},{},{},{},{}".format(line[1],line[2],y,s,d)
    outfile.write(row_string)
    outfile.write('\n')
outfile.close()
file.close()
