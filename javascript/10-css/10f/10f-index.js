function changeMode(event) {
    let button = event.target;

    if (button.classList.contains("js-button-off")) {
    button.classList.remove("js-button-off");
    button.classList.add("js-button-on");
    console.log("on");
    }
    else if (button.classList.contains("js-button-on"))  {
      button.classList.remove("js-button-on");
      button.classList.add("js-button-off");
      console.log("off");
    }
    else {
      console.log("button not found");
    }
  }