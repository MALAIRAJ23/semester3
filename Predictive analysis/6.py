year=[2001,2002,2003,2004,2005,2006]
attendees=[1.44,1.58,1.55,1.47,1.37,1.41]

def moving_average(attendees,period):
    avg=[]
    for i in range(len(year)):
        if i<period-1:
            avg.append("-")
        else:
            avg.append(sum(attendees[i-period+1:i+1])/period)
    return avg
def smoothing(attendees,alpha):
    smoothed= [attendees[0]]
    for t in range(1,len(attendees)):
        smoothed.append(alpha*attendees[t]+(1-alpha)*smoothed[-1])
    return smoothed
ma_3= moving_average(attendees, 3)
ma_5= moving_average(attendees, 5)
exp_1= smoothing(attendees, 0.5)
exp_2= smoothing(attendees, 0.25)

for i in range(len(year)):
    print(f"{year[i]}\t{attendees[i]:.2f}\t\t"
          f"{ma_3[i]}\t\t"
          f"{ma_5[i]}\t\t"
          f"{exp_1[i]:.2f}\t\t"
          f"{exp_2[i]:.2f}")