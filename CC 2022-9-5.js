// I have a cat and a dog.

// I got them at the same time as kitten/puppy. That was humanYears years ago.

// Return their respective ages now as [humanYears,catYears,dogYears]s

// NOTES:

//     humanYears >= 1
//     humanYears are whole numbers onlyf

// Cat Years

//     15 cat years for first year
//     +9 cat years for second year
//     +4 cat years for each year after that

// Dog Years

//     15 dog years for first year
//     +9 dog years for second year
//     +5 dog years for each year after thatf


//My solution

var humanYearsCatYearsDogYears = function(humanYears) {
    return [humanYears,(15 +  ((humanYears > 2) ? (9+(humanYears-2)*4) : humanYears == 2 ? 9 : 0)), (15 +  ((humanYears > 2) ? (9+(humanYears-2)*5) : humanYears == 2 ? 9 : 0)) ]
}