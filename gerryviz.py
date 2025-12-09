from election_results import results
import matplotlib.pyplot as plt
districts = []
republicans = []
democrats = []
x = 0
while x == 0:
    year = str(input('What year would you like to evaluate? '))
    districts = []
    republicans = []
    democrats = []
    if year in results.keys():
        state = str(input('What state would you like to evaluate? '))
            #makes the state given all uppercase because that is how the keys are
        state = state.upper()
            #checks to see if the state is a valid key according to the dictionary
        if state in results[year].keys():
            wasted_dem = 0
            wasted_rep = 0
            entire_total = 0
            for element in results[year][state]:
                districts.append(element.district.lstrip('0'))
                if element.rep_votes <element.dem_votes:
                    winner = element.dem_votes
                    loser = element.rep_votes
                    total = element.dem_votes + element.rep_votes
                    needed = total/2
                    wasted_dem = winner-needed
                    wasted_rep = element.rep_votes
                else:
                    winner = element.rep_votes
                    loser = element.dem_votes
                    total = element.dem_votes + element.rep_votes
                    needed = total/2
                    wasted_rep = winner-needed
                    wasted_dem = element.dem_votes
                republicans.append(wasted_rep)
                democrats.append(wasted_dem)           
            fig = plt.figure(figsize = (10, 5))
            plt.bar(districts,democrats,.6, label = 'Democratic', color = 'blue')
            plt.bar(districts,republicans,.6,bottom = democrats,label = 'Republican',color = 'red')
            plt.xlabel('District Number')
            plt.ylabel("Number of wasted votes")
            plt.title(f"Wasted Votes in {state} in {year} ")
            plt.legend()
            plt.show()
            y = str(input('Would you like to continue? Type Yes or No '))
            if y.upper() == 'YES':
                    #if they would like to continue, keep the while loop going
                    x = 0
            else:
                #if they would like to stop, stop the loop by adding to this variable
                x+= 1
        else:#if the state is inputted incorrectly, print this message
            print(f'{state} is not a valid state')
    else:
        print('Invalid year: please give an appropriate election year from 1976 to 2020')

