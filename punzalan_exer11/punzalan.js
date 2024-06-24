function randomizer(restaurant) {
  // FOR GENERATING RANDOM KEY
  const allKeys = Object.keys(restaurant);
  const restaurantKeyLength = allKeys.length; 
  const randomKeyIndex = Math.floor(Math.random() * restaurantKeyLength); // Generates a random integer ranging the length of the keys
  const generatedKey = allKeys[randomKeyIndex]; // Actual random key

  // FOR GENERATING RANDOM VALUE
  const randomValueIndex = Math.floor(Math.random() * restaurant[generatedKey].length) // Generates a random integer ranging the value of the random key
  const randomValue = restaurant[generatedKey][randomValueIndex]; // Actual random value


  return generatedKey + " : " + randomValue;
};



const restaurant = {
  Jollibee : ["Jolly Spaghetti", "1pc Chicken Joy", "Peach Mango Pie", "Aloha Yum Burger", "Palabok"],
  Mcdonalds : ["Hotcakes", "Cheesy Burger Mcdo", "Quarter Pounder", "Crispy Chicken Fllet", "Mc Spaghetti"],
  Chowking : ["Pork Chop Lauriat", "Chicken Lauriat", "Sweet and Sour Pork", "Pork Chow Fan", "Wanton Mami"]
};

