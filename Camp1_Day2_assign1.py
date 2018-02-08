Sessions_Attended = {'sessions' : '1011,2344,3222,44322,555,6332,721,'}
text = Sessions_Attended["sessions"]
count = len([session for session in text.split(',') if session.isdigit()])
print("I have attended " + str(count) + " sessions!!")
