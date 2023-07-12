

def readLogger():
    log_file = open('app.log', 'r')

    lines = log_file.readlines()

    i = 1
    for line in lines:
        print(i,"", line)
        i+=1
    log_file.close()

readLogger()