import EnvironmentAnalysis
import Agent
import pandas as pd
import MovingAgent
import Moving_Target
import Moving_TargetMoving_Agent
import Environment

IS_FLAT = 1
IS_HILLY = 2
IS_FOREST = 3
IS_CAVE = 4

typelist = [IS_FLAT, IS_HILLY, IS_FOREST, IS_CAVE]
dataRule1 = []
for celltype in typelist:
    for i in range(100):
        env = EnvironmentAnalysis.Environment(50, celltype)
        agent = Agent.Agent(env, 1, 50)
        dataRule1.append([celltype, agent.finalSteps])
        print("Iteration:", i)

Rule1DF = pd.DataFrame(dataRule1, columns=["Type", "NumberOfSteps"])
Rule1DF.to_csv("Rule1.csv", sep=',', encoding='utf-8', mode='a')

dataRule2 = []
for celltype in typelist:
    for i in range(100):
        env = EnvironmentAnalysis.Environment(50, celltype)
        agent = Agent.Agent(env, 2, 50)
        dataRule2.append([celltype, agent.finalSteps])
        print("Iteration:", i)

Rule2DF = pd.DataFrame(dataRule2, columns=["Type", "NumberOfSteps"])
Rule2DF.to_csv("Rule2.csv", sep=',', encoding='utf-8', mode='a')

dataRule1Moving = []
for celltype in typelist:
    for i in range(100):
        env = EnvironmentAnalysis.Environment(50, celltype)
        agent = MovingAgent.Agent(env, 1, 50)
        dataRule1Moving.append([celltype, agent.finalSteps])
        print("Iteration:", i)

Rule1MovingDF = pd.DataFrame(dataRule1Moving, columns=["Type", "NumberOfSteps"])
Rule1MovingDF.to_csv("Rule1Moving.csv", sep=',', encoding='utf-8', mode='a')

dataRule2Moving = []
for celltype in typelist:
    for i in range(100):
        env = EnvironmentAnalysis.Environment(50, celltype)
        agent = Agent.Agent(env, 2, 50)
        dataRule2Moving.append([celltype, agent.finalSteps])
        print("Iteration:", i)

Rule2MovingDF = pd.DataFrame(dataRule2Moving, columns=["Type", "NumberOfSteps"])
Rule2MovingDF.to_csv("Rule2Moving.csv", sep=',', encoding='utf-8', mode='a')

# For Question 2:
dataRule1 = []
for i in range(20):
    env = Environment.Environment(50)
    agent = Moving_Target.Moving_Target_Agent(env, 1, 50)
    dataRule1.append(agent.finalSteps)
    print("Iteration:", i)

Rule1DF = pd.DataFrame(dataRule1, columns=["NumberOfSteps"])
Rule1DF.to_csv("Rule1MovingTarget.csv", sep=',', encoding='utf-8', mode='a')

dataRule2 = []

for i in range(20):
    env = Environment.Environment(50)
    agent = Moving_Target.Moving_Target_Agent(env, 2, 50)
    dataRule2.append(agent.finalSteps)
    print("Iteration:", i)

Rule2DF = pd.DataFrame(dataRule2, columns=["NumberOfSteps"])
Rule2DF.to_csv("Rule2MovingTarget.csv", sep=',', encoding='utf-8', mode='a')

dataRule1Moving = []

for i in range(20):
    env = Environment.Environment(50)
    agent = Moving_TargetMoving_Agent.Moving_Target_Moving_Agent(env, 1, 50)
    dataRule1Moving.append(agent.finalSteps)
    print("Iteration:", i)

Rule1MovingDF = pd.DataFrame(dataRule1Moving, columns=["NumberOfSteps"])
Rule1MovingDF.to_csv("Rule1MovingTargetMovingAgent.csv", sep=',', encoding='utf-8', mode='a')

dataRule2Moving = []

for i in range(20):
    env = Environment.Environment(50)
    agent = Moving_TargetMoving_Agent.Moving_Target_Moving_Agent(env, 2, 50)
    dataRule2Moving.append(agent.finalSteps)
    print("Iteration:", i)

Rule2MovingDF = pd.DataFrame(dataRule2Moving, columns=["NumberOfSteps"])
Rule2MovingDF.to_csv("Rule2MovingTargetMovingAgent.csv", sep=',', encoding='utf-8', mode='a')
