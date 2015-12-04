function inputName(IelementId) {
    var person = prompt("Please enter your name", "Harry Potter");
    
    if (person != null) {
        document.getElementById(elementId).innerHTML =
        "Hello " + person + "! My name is Apple. I am shiba :)";
    }
}