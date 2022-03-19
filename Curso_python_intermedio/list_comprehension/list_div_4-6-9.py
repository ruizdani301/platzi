#****************************************************
# this code show all numbers divisible by 4 - 9 - 6 *
#****************************************************

def run():
    div =[i for i in range(1,1001) if i%4 == 0 and i%6 == 0 and i%9 == 0]
    print(div)

if __name__ == "__name__":
	run()