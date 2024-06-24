let forForm = document.forms['pizza-form'];

// for time
const deliveryTime = document.getElementById('time');

deliveryTime.addEventListener('change', function(event) {
	if (time.value < '10:00' || time.value > '19:00') {
		alert('Delivery time should be after 10:00AM or before 7:00PM.')
	};
});


// for pizza size
let pizaSize = new Array();
pizaSize["small-size"] = 125;
pizaSize["medium-size"] = 250;
pizaSize["large-size"] = 500;

function getPizzaSize() {
	let pizzaSizePrice = 0;
	let forForm = document.forms["pizza-form"];

	let selectedSize = forForm.elements["size"]

	for(let i = 0; i < selectedSize.length; i++) {
		if(selectedSize[i].checked) {
			pizzaSizePrice = pizaSize[selectedSize[i].value];
			break;
		}
	}
	return pizzaSizePrice;
}


// for pizza crust
let pizaCrust = new Array();
pizaCrust["thin-crust"] = 50;
pizaCrust["thick-crust"] = 70;

function getCrustType() {
	let pizzaCrustPrice = 0;
	let forForm = document.forms["pizza-form"];

	let selectedCrustType = forForm.elements["type"]

	for(let i = 0; i < selectedCrustType.length; i++) {
		if(selectedCrustType[i].checked) {
			pizzaCrustPrice = pizaCrust[selectedCrustType[i].value];
			break;
		}
	}
	return pizzaCrustPrice;
}


// for main toppings
let mainTopping = new Array();
mainTopping["pep-overload"] = 100;
mainTopping["hawaiian"] = 50;
mainTopping["meat-overload"] = 125;

function getMainToppingPrice() {
	let pizzaMainToppingPrice = 0
	let forForm = document.forms["pizza-form"];

	let selectedMainTopping = forForm.elements["topping-list"]
	pizzaMainToppingPrice = mainTopping[selectedMainTopping.value];

	return pizzaMainToppingPrice
}


// for additional toppings
function getAdditionalToppingPrice() {
	let vegetablePrice = 0;
	let meatPrice = 0;
	let cheesePrice = 0;

	let forForm = document.forms["pizza-form"];

	let selectedVegetable = forForm.elements["vegetables"];
	let selectedMeat = forForm.elements["meat"];
	let selectedCheese = forForm.elements["cheese"];

    if (selectedVegetable.checked == true) vegetablePrice = 12;
	if (selectedMeat.checked == true) meatPrice = 75;
	if (selectedCheese.checked == true) cheesePrice = 50;

	totalAdditionalToppingPrice = vegetablePrice + meatPrice + cheesePrice

    return totalAdditionalToppingPrice;
}


const forSizePizza = document.addEventListener('click', function (event) {
	document.getElementById('pizza-size').innerHTML = getPizzaSize()
});

const forCrustPizza = document.addEventListener('click', function (event) {
	document.getElementById('crust-type').innerHTML = getCrustType()
});

const forMainTopping = document.addEventListener('click', function (event) {
	document.getElementById('main-toppings').innerHTML = getMainToppingPrice()
});

const forAdditionalTopping = document.addEventListener('click', function (event) {
	document.getElementById('additional-toppings').innerHTML = getAdditionalToppingPrice()
});


let totalNoTax = document.addEventListener('click', function (event) {
	document.getElementById('total-no-tax').innerHTML = getPizzaSize() + getCrustType() + getMainToppingPrice() + getAdditionalToppingPrice()
});

const totalWithTax = document.addEventListener('click', function (event) {
	document.getElementById('total-w-tax').innerHTML = (getPizzaSize() + getCrustType() + getMainToppingPrice() + getAdditionalToppingPrice()) + ((getPizzaSize() + getCrustType() + getMainToppingPrice() + getAdditionalToppingPrice()) * .12)
});