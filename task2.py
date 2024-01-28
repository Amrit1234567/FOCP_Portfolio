import sys
def analysis(ours, theirs, length):    
    print("Log File Analysis")
    print("="*17)
    print(f"Cat Visits {ours}")
    print(f"Other Cats {theirs}")
    print(f"\nTotal Time in House: {sum(length)//60} Hours, {sum(length)%60} Minute") if sum(length)%60 <=1 else print(f"\nTotal Time in House: {sum(length)//60} Hours, {sum(length)%60} Minutes")
    print(f"\nAverage Visit Length: {sum(length)//len(length)} Minutes")
    print(f"Longest Visit: {max(length)} Minutes")
    print(f"Shortest Visit: {min(length)} Minute") if min(length) <= 1 else print(f"Shortest Visit: {min(length)} Minutes")


if __name__ == "__main__":
    data_lst = []
    length = []

    f = open(sys.argv[1])
    for x in f.readlines():
        data = x.strip()
        data_lst.append(data.split(","))
    
    f.close()
    theirs, ours = 0,0

    for x in data_lst:
        if x[0]=="THEIRS":
            theirs += 1
        elif x[0] == "OURS":
            ours +=1
            duration = int(x[2]) - int(x[1])
            length.append(duration)

    analysis(ours, theirs, length)