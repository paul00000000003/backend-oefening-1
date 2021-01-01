# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line
scorer_name_0="Gullit"
scorer_name_1="van Basten"
goal_0=32
goal_1=54
print(scorer_name_0," ",str(goal_0),',',scorer_name_1," ",str(goal_1))
report=(f'{scorer_name_0} scored in the {goal_0}-th minute \n {scorer_name_1} scored in the {goal_1}-th minute')
print(report)
player="Marco van Basten"
firstname_player=player[0:player.find(" ")]
print(firstname_player)
last_name_len=len(player)-len(player[0:player.find(" ")])-1
print("lengte achternaam : "+str(last_name_len))

name_short=player[0:1]+". "+player[len(firstname_player)+1:]
print(name_short)
chant=f'{firstname_player}! '*(len(firstname_player)-1)+f'{firstname_player}!'
print(chant)

if (chant[len(chant):1] != " ") : print("laatste karakter geen spatie")


