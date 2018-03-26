Time = input()
Hour = Time //60
Time %= 60
Minutes = Time // 1
print("h:m-> %d:%d" % (Hour,Minutes))
