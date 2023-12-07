initial_state = ["OFF"] * 16
schedule = {}

def switch_on(index):
    initial_state[index] = "ON"
    print("Switch" ,(index+1), "is turned ON")

def switch_off(index):
    initial_state[index] = "OFF"
    print("Switch" ,(index+1), "is turned OFF")
    
def schedule_switch(index, action, hour):
    schedule[index] = (hour, action)
    
def sense_state(z):
    if z == 'ALL':
        for i in range(len(initial_state)):
            print((i+1),"-",(initial_state[i]))
    else:
        print(initial_state[int(z)-1])

while True:
    cmd = input("Enter command: ").split()
    if 'ON' in cmd:
        index = int(cmd[0]) - 1
        if len(cmd) == 2:
            switch_on(index)
        else:
            hour = cmd[3]
            schedule_switch(index, 'ON', hour)
            print("Switch" ,(index+1), "will be turned ON at" ,hour)
    elif 'OFF' in cmd:
        index = int(cmd[0]) - 1
        if len(cmd) == 2:
            switch_off(index)
        else:
            hour = cmd[3]
            schedule_switch(index, 'OFF', hour)
            print("Switch" ,(index+1), "will be turned OFF at" ,hour)
            
    elif 'TIME' in cmd:
        time = cmd[1]
        print("Time is set to" ,time)
        for index, (hour, action) in dict(schedule).items():
            if hour == time:
                if action == 'ON':
                    switch_on(index)
                else:
                    switch_off(index)
                    
    elif '?' in cmd:
        sense_state(cmd[1])
        
    elif cmd[0] == 'STOP':
        print('Simulation halts')
        break

    
            
