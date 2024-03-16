//https://www.codewars.com/kata/find-the-smallest-integer-in-the-array/train/javascript
class SmallestIntegerFinder {
  findSmallestInt(args) {
    return Math.min(...args);
  }
}

//https://www.codewars.com/kata/geometry-basics-circle-circumference-in-2d/train/javascript
function circleCircumference(circle) {
  return Math.round(2 * circle.radius * Math.PI * 1000000) / 1000000;
}

//https://www.codewars.com/kata/training-js-number-12-loop-statement-for-dot-in-and-for-dot-of/train/javascript
function giveMeFive(obj) {
  // Other version
  // return Object.keys(obj).filter(key => key.length === 5)
  //.concat(Object.values(obj).filter(val => val.length === 5));
  let result = [];
  for (let key in obj) {
    if (key.length === 5) {
      result.push(key);
    }
    if (obj[key].length === 5) {
      result.push(obj[key]);
    }
  }
  return result;
}
