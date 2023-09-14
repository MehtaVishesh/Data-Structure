def countUserLogins(logs):
    table = []
    LookedAtLogs = {}
    for log in logs:
        if (str(log[0]) + str(log[1])) not in LookedAtLogs.keys():
            LookedAtLogs[str(log[0]) + str(log[1])] = 1
        else:
            LookedAtLogs[str(log[0]) + str(log[1])] += 1
    
    for log in LookedAtLogs.keys():
        table.append([log, LookedAtLogs[log]])
        
    return table

t = countUserLogins(["user1", "12/03/23", "832;"])
print(t)