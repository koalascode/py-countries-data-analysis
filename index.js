function handleAll() {
    selectThree = document.getElementById("selectThree")
    selectFour = document.getElementById("selectFour")
    selectFive = document.getElementById("selectFive")
    amountInput = document.getElementById("amountinput")

    console.log(selectThree.value)

    if (selectThree.value === '0') {
        selectFive.style.display = "none"
        console.log("Select 3 Value is 0")
    }

    if (selectThree.value === '4' || selectThree.value === '5') {
        amountInput.style.display = "block"
        console.log("Select 3 Value is 4 or 5")
    } else {
        amountInput.style.display = "none"
    }

    console.log(" THE FUNCTION IS WORKING CORRECTLY!! I REPEAT, THE FUNCTION IS WORKING CORRECTLY! ")
}

