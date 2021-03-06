# bb_stats.py
# Bob Staten
# 4/21/2019
# a python program to calculate a running batting average

# a program for calculating a running batting for a single plater

base_hits = []
at_bats = []
runs = []

def stats_j(hits,abs,rbis):

#append arguments to lists
  base_hits.append(hits)
  at_bats.append(abs)
  runs.append(rbis)

# calculations
  tot_rbis = sum(runs)
  avg = int(round(sum(base_hits) / sum(at_bats), 3) * 1000)

  return ('Batting avg: %s' % avg + '\n' + ' ' + 'Runs batted in: %d' % tot_rbis)

# execution
# TODO create a file to store data, and use it to update average.
# here's the problem. I want to store stats in a file instead of keeping them in the code itself as below

# Spring 2019 - Rookie
#stats_j(2,3,1) # 4/6/19
#stats_j(1,3,2) # 4/9/19
#stats_j(1,4,1) # 4/15/19
#stats_j(2,3,2) # 4/18/19
#stats_j(2,3,2) # 4/23/19
#stats_j(2,3,1) # 4/25/19
#stats_j(2,3,0) # 4/27/19
#stats_j(5,5,3) # 5/4/19
#stats_j(1,4,0) # 5/11/19
#stats_j(2,3,1) # 5/17/19
#stats_j(0,3,0) # 5/18/19
#stats_j(4,5,2) #5/21/19

# Fall 2019 - Rookie
stats_j(2,3,1) #8/20/19
stats_j(1,3,0) #8/22/19
stats_j(3,3,0) #8/24/19
stats_j(1,1,0) #9/12/19
stats_j(3,4,0) #9/19/19
print(stats_j(3,3,1)) #9/21/19
