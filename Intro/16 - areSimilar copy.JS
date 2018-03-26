/*
Two arrays are called similar if one can be obtained from another by swapping at most one pair of elements in one of the arrays.

Given two arrays a and b, check whether they are similar.

Example

For a = [1, 2, 3] and b = [1, 2, 3], the output should be
areSimilar(a, b) = true.

The arrays are equal, no need to swap any elements.

For a = [1, 2, 3] and b = [2, 1, 3], the output should be
areSimilar(a, b) = true.

We can obtain b from a by swapping 2 and 1 in b.

For a = [1, 2, 2] and b = [2, 1, 1], the output should be
areSimilar(a, b) = false.

Any swap of any two elements either in a or in b won't make a and b equal.
*/

//===Solution in Javascript===

function areSimilar(a, b) {
    //Compare the arrays
    //Must convert to strings to compare as a== b will return false
    if (a.toString() == b.toString()) {
        return true;
    }
    //Create two arrays to store changed values
    var c = [];
    var d = [];
    //Iterate through arrays
    for (var i = 0; i < a.length; i++) {
        //If a value is not the same in a or b
        //Add the value of each to the array
        if (a[i] != b[i]) {
            c.push(a[i]);
            d.push(b[i]);
        }
    }
    //Reverse the array to compare later
    d = d.reverse();
    //c.length means 1 swap occured as two values didnt add up
    //compare the reversed d array to c array for the same values meanigng we can 
    if (c.length === 2 && (c.toString() == d.toString())) {
        return true;
    }
    return false;
}

///========================