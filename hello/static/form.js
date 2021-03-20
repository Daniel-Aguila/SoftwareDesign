// const init = function(){
//     document.getElementById('button-cancel').addEventListener('click',reset);
//     document.getElementById('button-send').addEventListener('click',send);
// }

const reset = function(ev){
    ev.preventDefault();
    document.getElementById('form-user').reset();
}

const send = function(ev){
    ev.preventDefault();
    ev.stopPropagation();

    let fails = validate();

    if(fails.length===0){
        //good
        document.getElementById('form-user').submit();
    }
    else{
        //bad
        fails.forEach(function(obj){
            let field = document.getElementById(obj.input);
            field.parentElement.classList.add('error');
            field.parentElement.setAttribute('data-errormsg', obj.msg);
        })
    }
}

const validate = function(ev){

    let failures = [];
    let gallons = document.getElementById("input-gallons"); // extract gallons entry
    var gal_Value = gallons.value;
    let address = document.getElementById("input-address"); // extract address
    if(gal_Value < 0){
        failures.push({input:'input-gallons', msg:'not enough'});
    }
    if(address.value === ""){
        failures.push({input:'input-address',msg:'Required Field'});
    }
    return failures;
}

//document.addEventListener('DOMContentLoaded',init);

// -----------

document.querySelector('#input-gallons-input').value = 0;

const submit = document.querySelector('#form-submit');

submit.addEventListener('click', function(e) {
    e.preventDefault();
  
    alert('HELLO')//TARGET MESSAGE
    let gallonsInput = document.querySelector('#input-gallons-input').value; 
    if (gallonsInput < 1)
    {
        alert('Please input valid number of gallons')
        return;
    }
    else
    {
        alert('SUBMIT SUCCESS');
        let historyRedirect = 'http://' + window.location.host + '/history';
        window.location.href = historyRedirect;
    }
})
