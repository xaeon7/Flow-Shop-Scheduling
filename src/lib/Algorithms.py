
###! Function - START
def Johnson(M1, M2):
    Jobs = [M1, M2]

    U= [j for j in range(len(Jobs[0])) if Jobs[0][j] <= Jobs[1][j]]
    V = [j for j in range(len(Jobs[0])) if Jobs[0][j] > Jobs[1][j]]

    U = sorted(U, key=lambda i: Jobs[0][i])
    V = sorted(V, key=lambda i: Jobs[1][i], reverse=True)
    
    sigma = [sum(x) for x in zip(U+V, [1] * len(Jobs[0]))]
    
    return sigma
###! Function - END


###! Function - START
def getMakespan(Jobs, sequence):
    C = []
    for machine in range(0, len(Jobs)):
        C.append([])
        for idx, job in enumerate(sequence):
            if machine == 0 and idx == 0:
                C[machine].append(Jobs[machine][job - 1])
            elif idx == 0:
                C[machine].append(Jobs[machine][job - 1] + C[machine - 1][idx])
            else : 
                if machine == 0:
                    C_max = C[machine][idx - 1]
                else :
                    C_max = max(C[machine][idx - 1], C[machine - 1][idx])
                C[machine].append(C_max + Jobs[machine][job - 1])
    return C
###! Function - END


###! Function - START
def getStartTime(Jobs, sequence, C):
    Start = []
    for machine in range(0, len(Jobs)):
        Start.append([])
        for idx, job in enumerate(sequence):
            if machine == 0 and idx == 0:
                Start[machine].append(0)
            elif idx == 0:
                Start[machine].append(C[machine - 1][idx])
            else : 
                if machine == 0:
                    C_max = C[machine][idx - 1]
                else :
                    C_max = max(C[machine][idx - 1], C[machine - 1][idx])
                Start[machine].append(C_max)
    return Start
###! Function - END


###! Function - START
###? Get makespan with preparation time (Sequence Dependent Setup Time)
def getMakespanSDST(Jobs, SDST, sequence):
    C = []
    for machine in range(0, len(Jobs)):
        C.append([])
        for idx in range(0, len(sequence)):
            if machine == 0 and idx == 0:
                C[machine].append(Jobs[machine][sequence[idx] - 1] + SDST[machine][sequence[idx] - 1][sequence[idx] - 1])
            elif machine == 0 and idx != 0:
                C[machine].append(Jobs[machine][sequence[idx] - 1] + SDST[machine][sequence[idx - 1] - 1][sequence[idx] - 1] + C[machine][idx - 1])
            elif idx == 0 and machine != 0:
                C_max = max(SDST[machine][sequence[idx] - 1][sequence[idx] - 1], C[machine - 1][idx])
                C[machine].append(Jobs[machine][sequence[idx] - 1] + C_max)
            else:
                C_max = max(SDST[machine][sequence[idx - 1] -1][sequence[idx] - 1] + C[machine][idx - 1], C[machine - 1][idx])
                C[machine].append(Jobs[machine][sequence[idx] - 1] + C_max)
    return C
###! Function - END


###! Function - START
def getStartTimeSDST(Jobs, SDST, sequence, C):
    Start = []
    for machine in range(0, len(Jobs)):
        Start.append([])
        for idx in range(0, len(sequence)):
            if machine == 0 and idx == 0:
                Start[machine].append(0)
            elif machine == 0 and idx != 0:
                Start[machine].append(SDST[machine][sequence[idx - 1] - 1][sequence[idx] - 1] + C[machine][idx - 1])
            elif idx == 0 and machine != 0:
                C_max = max(SDST[machine][sequence[idx] - 1][sequence[idx] - 1], C[machine - 1][idx])
                Start[machine].append(C_max)
            else:
                C_max = max(SDST[machine][sequence[idx - 1] -1][sequence[idx] - 1] + C[machine][idx - 1], C[machine - 1][idx])
                Start[machine].append(C_max)
    return Start
###! Function - END


###! Function - START
def getNewMachines(Jobs, stage):
    n_seq = len(Jobs) - 1

    if stage == 0:
        return [Jobs[0], Jobs[n_seq]]

    else:
        newMachine1 =  [a + b for a, b in zip(getNewMachines(Jobs, stage - 1)[0], Jobs[stage])]
        newMachine2 =  [a + b for a, b in zip(getNewMachines(Jobs, stage - 1)[1], Jobs[n_seq - stage])]

        return [newMachine1, newMachine2]
###! Function - END
