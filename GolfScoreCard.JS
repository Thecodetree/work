var names = ("Hole in one", "Eagle", "Birdie", "Par", "Bogey", "Double Bogey", "You Blew It!");
function golfScore(par, strokes) {
    if (strokes <= 1) {
    return "Hole in one";
    }else if (strokes <= par -2) {
  return "eagle";  
    }else if (strokes <= par -1) {
    return "Birdie";
    }else if (strokes === par) {
    return "Par";
    }else if (strokes === par +1) {
    return "Bogey";
    }else if (strokes === par +2) {
    return "Double Bogey";
    }else if (strokes >= par +3) {
    return "You Blew It!";

    
}

return "Change me";
}

golfScore(4, 4)

console.log(golfScore(4, 7));