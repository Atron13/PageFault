# Python3 program for implementation  
# of FCFS scheduling 
  
# Function to find the waiting  
# time for all processes


def findWaitingTime(n,tat,bt): 
  
    # waiting time for  
    # first process is 0
    wt = [0] * n 
    wt[0]=0
    # calculating waiting time 
    for i in range(0, n): 
        wt[i] = tat[i] - bt[i] 

    return wt
  
# Function to calculate turn 
# around time 
def findTurnAroundTime(n,compt,at): 
  
    # calculating turnaround  
    # time by adding bt[i] + wt[i]
    tat=[0]*n

    for i in range(0,n): 
        tat[i] = compt[i] - at[i]

    return tat
  
# Function to calculate 
# average time 
def complete(n,bt):
    compt=[0]*n
    #for i in range(0, n): 
        #compt[i] = bt[i]+compt[i]
        #print(compt[i])

    compt[0]=bt[0]
    compt[1]=bt[0]+bt[1]
    compt[2]=bt[0]+bt[1]+bt[2]
    compt[3]=bt[0]+bt[1]+bt[2]+bt[3]
    compt[4]=bt[0]+bt[1]+bt[2]+bt[3]+bt[4]
    compt[5]=bt[0]+bt[1]+bt[2]+bt[3]+bt[4]+bt[5]
    return compt

def findavgTime( processes, n, bt): 
  
    wt = [0] * n 
    tat = [0] * n  
    total_wt = 0
    total_tat = 0
  
    # Function to find waiting  
    # time of all processes 
    findWaitingTime(processes, n, bt, wt) 
  
    # Function to find turn around  
    # time for all processes 
    #findTurnAroundTime(processes, n,  
                       #bt, wt, tat) 
  
    # Display processes along 
    # with all details 
    print( "Processes Burst time " + 
                  " Waiting time " + 
                " Turn around time") 
  
    # Calculate total waiting time  
    # and total turn around time 
    for i in range(n): 
      
        total_wt = total_wt + wt[i] 
        total_tat = total_tat + tat[i] 
        print(" " + str(i + 1) + "\t\t" + 
                    str(bt[i]) + "\t " + 
                    str(wt[i]) + "\t\t " + 
                    str(tat[i]))  
  
    print( "Average waiting time = "+
                   str(total_wt / n)) 
    print("Average turn around time = "+
                     str(total_tat / n)) 
  
# Driver code 
      
    # process id's 
    # Burst time of all processes 
    #burst_time = [10, 5, 8] 
  
    #findavgTime(processes, n, bursttime)