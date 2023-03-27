const ages = [7, 18, 35, 39, 69];
const result = ages.filter(checkLegalAge);

function checkLegalAge(age) {
    return age >= 21;
}