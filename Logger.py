def log_it(content):
    content = str(content)
    f = open("logfile.txt", "a")
    f.write(content+"\n")
    f.close()