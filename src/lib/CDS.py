from lib.Algorithms import *


class FlowShopSchedule():
    def __init__(self, jobs):
        self.jobs = jobs 
        self.sequence = []
        self.timeMatrixStart = []
        self.timeMatrix = []
        self.makespan = 0
        self.totalTardiness = 0
        self.operatingRate = []
        self.stopPreparationRate = []
        self.stopRate = []
        
    def __getOperatingRate(self):
        self.operatingRate =[sum(self.jobs[i]) / self.makespan for i in range(0, len(self.jobs))]    
        self.stopRate = [1 - (sum(self.jobs[i]) / self.makespan) for i in range(0, len(self.jobs))]
        
    def __getOperatingPreparationRate(self, SDST):
        self.operatingRate =[sum(self.jobs[i]) / self.makespan for i in range(0, len(self.jobs))] 
        
        
        for i in range(len(SDST)):
            s = self.sequence
            temp = SDST[i][s[0] - 1][s[0] - 1] 
            
            for j in range(1, len(SDST[0])):
                temp = temp + SDST[i][s[j-1] - 1][s[j] - 1] 
                
            self.stopPreparationRate.append(temp/self.makespan)
             
        self.stopRate = [1 - self.operatingRate[i] - self.stopPreparationRate[i] for i in range(0, len(self.jobs))]
        
    def CDS(self):
        machines = len(self.jobs)
        n_seq = machines - 1
        
        self.timeMatrix = []
        self.sequence = []
        
        for stage in range(0, n_seq):
            newJobs = getNewMachines(self.jobs, stage)
            sigma = Johnson(newJobs[0], newJobs[1]) 
            
            C = getMakespan(self.jobs, sigma)
            if stage == 0 or C[-1][-1] < self.timeMatrix[-1][-1]:
                self.timeMatrix = C
                self.sequence =  sigma
                self.makespan = C[-1][-1]
        
        self.__getOperatingRate()
        self.timeMatrixStart = getStartTime(self.jobs, self.sequence, self.timeMatrix)
                
    def Delay(self, DueDate, optimizeMakespan = 1):
        
        if optimizeMakespan == 1 :
            self.CDS()
            self.totalTardiness = sum([a - b if a - b > 0 else 0 for a, b in zip(self.timeMatrix[-1], DueDate)])
        
        else :
            machines = len(self.jobs)
            n_seq = machines - 1
            self.totalTardiness = float('inf')
            
            for stage in range(0, n_seq):
                newJobs = getNewMachines(self.jobs, stage)
                sigma = Johnson(newJobs[0], newJobs[1]) 
                
                C = getMakespan(self.jobs, sigma)
                TT = sum([a - b if a - b > 0 else 0 for a, b in zip(C[-1], DueDate)])
                
                if stage == 0:
                    self.timeMatrix = C
                    self.sequence = sigma
                    self.makespan = C[-1][-1]
                    
                if TT < self.totalTardiness:
                    self.timeMatrix = C
                    self.totalTardiness = TT
                    self.sequence = sigma
                    self.makespan = C[-1][-1]

        self.__getOperatingRate()
        self.timeMatrixStart = getStartTime(self.jobs, self.sequence, self.timeMatrix)
    
    def Preparation(self, SDST, properTime = 0):
        
        if properTime == 1:
            self.CDS()
            
        else:
            prepTime = []
            for j in range(0, len(SDST)):
                diag = [ SDST[j][i][i] for i in range(len(SDST[0]))]
                prepTime.append(diag)

            TP = [a + b for a, b in zip(prepTime[0], self.jobs[0])]
            for i in range(1, len(self.jobs)):
                prepJobs = [a + b for a, b in zip(prepTime[i], self.jobs[i])]
                TP =  [a + b for a, b in zip(TP, prepJobs)]

            self.sequence = [i[0] + 1 for i in sorted(enumerate(TP), key=lambda x:x[1], reverse= True)]
                
        self.timeMatrix = getMakespanSDST(self.jobs, SDST, self.sequence)       
        self.makespan = self.timeMatrix[-1][-1]
        self.__getOperatingPreparationRate(SDST)
        self.timeMatrixStart = getStartTimeSDST(self.jobs, SDST, self.sequence, self.timeMatrix)
        
    def PreparationAndDelay(self, SDST, DueDate, properTime = 0):
        self.Preparation(SDST, properTime)
        self.totalTardiness = sum([a - b if a - b > 0 else 0 for a, b in zip(self.timeMatrix[-1], DueDate)])
        self.timeMatrixStart = getStartTimeSDST(self.jobs, SDST, self.sequence, self.timeMatrix)
        
        

        