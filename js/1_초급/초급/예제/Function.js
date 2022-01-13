var add = function(num1,num2){
    return num1+num2
} // ==>
var add = (num1,num2) => num1+num2

showError()
function showError(){
    console.log('Error')
}

var showError = () =>{ console.log('Errors') }
showError()