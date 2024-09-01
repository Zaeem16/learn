let activeButton = null;

function changeMode(event) {
    let button = event.target;

    if (activeButton === button) {
        return; 
    }

    if (activeButton) {
        activeButton.classList.remove("js-button-on");
        activeButton.classList.add("js-button-off");
    }
    
    button.classList.remove("js-button-off");
    button.classList.add("js-button-on");

    activeButton = button; 
}
