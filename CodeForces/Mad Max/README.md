To finish his latest adventure, Max needs to ride from the Citadel to Gas Town. The last mad getaway from the remnants of Joe's army has left him almost without fuel, with little hope of making it all the way through. However, he has a plan — get the fuel along the way!

The two settlements are connected by a straight road. Along the road, there are nnn hitchhiker posts. The post number one is located at the Citadel, and the post number nnn at Gas Town. Along the road mmm hitchhikers wait for the passing vehicles. Hitchhiker number iii stands at post aiaia\_i and wants to get to some other post bibib\_i closer to Gas Town. When passing by each of the posts, Max can decide to give a lift to one the hitchhikers waiting there. If that happens they immideately give him fifif\_i liters of gasoline and give him cicic\_i cans of dog food, which is a popular barter commodity on the wasteland.

Max recently installed an archotech engine into his car. Thanks to that, regardless of the load he only have to expend one liter of fuel to travel between any two adjacent posts. However, due to the peculiarities of the constructions his car can only fit one passenger now, which means that he can accomodate only one hitchhiker at a time.

Max values his reputation, so if he decides to lift someone he must drop them off exactly at the location where they want to go. Additionally, he is in a bit of a rush, so he will only travel towards Gas Town. Finally, his car can hold any amount of dog food cans and gasoline thanks to the movie magic!

Your task is to check whether Max can get to his destination by helping the hitchhikers, and if so find the maximum amount of dog food that he can earn along the way.

Input

The first line contains three integers: 2≤n≤20002≤n≤20002 \\leq n \\leq 2000, 0≤m≤20000≤m≤20000 \\leq m \\leq 2000 and 0≤f≤1090≤f≤1090 \\leq f \\leq 10^9 — the number of posts, hitchhikers and the initial amount of liters of gasoline that Max has.

Next follow mmm lines. Line number iii contains the description of the hitchhiker number iii — integers 1≤ai≤n−11≤ai≤n−11 \\leq a\_i \\leq n - 1, 2≤bi≤n2≤bi≤n2 \\leq b\_i \\leq n, 0≤ci≤1090≤ci≤1090 \\leq c\_i \\leq 10^9 and 0≤fi≤1090≤fi≤1090 \\leq f\_i \\leq 10^9 being respectively the post number where the hitchhiker stands, their destination and amounts of dog food in cans and gasoline in liters that they are willing to pay. It is guaranteed that ai<biai<bia\_i < b\_i.

Output

If Max cannot reach Gas Town by any means, output "Impossible" (case sensitive). Otherwise, output a single non-negative integer — the number of dog food cans that Max can earn along the way.