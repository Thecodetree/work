const numbers = [21.8, 8.7, 3.1, 7.4];
document.getElementById("fun").innerHTML = numbers.reduce(getSum, 0);

function getSum(total, num) {
  return total + Math.round(num);
}