#!/usr/bin/node
module.exports = {
  /**
   * addMeMaybe - Invokes a function after incrementing its argument by 1.
   * @param {Number} number - The given function's argument.
   * @param {Number} theFunction - The function to be invoked.
   */
  addMeMaybe: function (number, theFunction) {
    number++;
    theFunction(number);
  }
};
