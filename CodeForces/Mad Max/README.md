# Mad Max: Hitchhikers Road

## Problem Description

To finish his latest adventure, Max needs to ride from the Citadel to Gas Town. The last mad getaway from the remnants of Joe's army has left him almost without fuel, with little hope of making it all the way through. However, he has a plan — get the fuel along the way!

The two settlements are connected by a straight road. Along the road, there are n
 hitchhiker posts. The post number one is located at the Citadel, and the post number n
 at Gas Town. Along the road m
 hitchhikers wait for the passing vehicles. Hitchhiker number i
 stands at post ai
 and wants to get to some other post bi
 closer to Gas Town. When passing by each of the posts, Max can decide to give a lift to one the hitchhikers waiting there. If that happens they immideately give him fi
 liters of gasoline and give him ci
 cans of dog food, which is a popular barter commodity on the wasteland.

Max recently installed an archotech engine into his car. Thanks to that, regardless of the load he only have to expend one liter of fuel to travel between any two adjacent posts. However, due to the peculiarities of the constructions his car can only fit one passenger now, which means that he can accomodate only one hitchhiker at a time.

Max values his reputation, so if he decides to lift someone he must drop them off exactly at the location where they want to go. Additionally, he is in a bit of a rush, so he will only travel towards Gas Town. Finally, his car can hold any amount of dog food cans and gasoline thanks to the movie magic!

Your task is to check whether Max can get to his destination by helping the hitchhikers, and if so find the maximum amount of dog food that he can earn along the way.

## Input

The first line contains three integers: 2≤n≤2000, 0≤m≤2000, and 0≤f≤10^9 — the number of posts, hitchhikers, and the initial amount of liters of gasoline that Max has.

Next follow m lines. Line number i contains the description of the hitchhiker number i — integers 1≤ai≤n−1, 2≤bi≤n, 0≤ci≤10^9, and 0≤fi≤10^9 being respectively the post number where the hitchhiker stands, their destination, and amounts of dog food in cans and gasoline in liters that they are willing to pay. It is guaranteed that ai<bi.

## Output

If Max cannot reach Gas Town by any means, output "Impossible" (case sensitive). Otherwise, output a single non-negative integer — the number of dog food cans that Max can earn along the way.

## Note
It doesn't matter how much gas Max will have when he reaches Gas Town, as long as he can do it.

Keep in mind the possibility of integer overflow.

In the first example, to get 4
 cans of dog food, Max expends all of his fuel to reach the post number 2
, where he picks up the only hitchhiker standing there. They give Max 1
 liter of gasoline, which he expends to reach Gas Town where he drops the hitchhiker off. He could have instead picked up the hitchhiker at post 1
, but then he would only earn 3
 cans since he wouldn't be able to pick up the hitchhiker at post 2
 since he cannot travel back.
