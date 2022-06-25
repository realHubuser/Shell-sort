import random
amogus=random.sample(range(-100, 100), 10)
print("input array:",amogus)
def shellSort(among, us):
	sus=us//2
	
	
	while sus>0:
		imposter=sus
		while imposter<us:
			crewmate=imposter-sus
			
			while crewmate>=0:
				if among[crewmate+sus]>among[crewmate]:

					break
				else:
					among[crewmate+sus],among[crewmate]=among[crewmate],among[crewmate+sus]

				crewmate=crewmate-sus
			imposter+=1
		sus=sus//2
shellSort(amogus,len(amogus))
print("sorted array:",amogus)