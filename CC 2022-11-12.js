/*Given the a list of numbers, return a fixed list so that the values increment by 1 for each index from the minimum value up to the maximum value (both included). */
function pipeFix(numbers){
	let arr = [];
	for (let i = numbers[0]; i <= numbers[numbers.length - 1]; i++) {
		arr.push(i);
	}
	return arr;
}