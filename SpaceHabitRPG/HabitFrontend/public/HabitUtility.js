function HabitUtilities() {
    var self = this;

    self.arrayRandomChoice = function (array) {
        return array[Math.floor(Math.random() * array.length)];
    }
}