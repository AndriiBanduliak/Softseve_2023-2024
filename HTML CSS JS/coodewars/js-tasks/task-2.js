//https://www.codewars.com/kata/convert-a-string-to-an-array/train/javascript
function stringToArray(string) {
  return string.split(" ");
}

//https://www.codewars.com/kata/dna-to-rna-conversion/train/javascript
function DNAtoRNA(dna) {
  return [...dna].map((dnaPart) => (dnaPart === "T"? (dnaPart = "U"): dnaPart)).join("");
}

//https://www.codewars.com/kata/577a98a6ae28071780000989/train/javascript
var min = function (list) {
  return [...list].sort((a, b) => a - b)[0];
};

var max = function (list) {
  return [...list].sort((a, b) => a - b).reverse()[0];
};

//https://www.codewars.com/kata/544a54fd18b8e06d240005c0/train/javascript
function min(arr, toReturn) {
  return toReturn === "value"? Math.min(...arr): arr.indexOf(Math.min(...arr));
}
