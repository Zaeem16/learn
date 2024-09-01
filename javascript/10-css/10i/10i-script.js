let calcHistory = localStorage.getItem("calculation")
    if (calcHistory === null) {
    calcHistory = '';
    }
    let calculation = '';
    let operators = ['+', '-' , '*', '/'];
    let calculator = document.querySelector(".js-calculation");
    
    function updateCalc(calc) {
    if (operators.includes(calc)) {
        calculation += " " + calc + " ";
        
    } else {
    calculation += calc;
    }
    
    calculator.innerHTML = calculation;
    }
    
    
    function calcResult() {
    calculation = eval(calculation);
    calculator.innerHTML = calculation;
    localStorage.setItem("calculation", calculation);
    }

    function clearCalc() {
    calculation = '';
    calculator.innerHTML = calculation;
    }

    calculation = calcHistory;
    calculator.innerHTML = calculation;