// const init = function(){
//     document.getElementById('button-cancel').addEventListener('click',reset);
//     document.getElementById('button-send').addEventListener('click',send);
// }

// const reset = function(ev){
//     ev.preventDefault();
//     document.getElementById('form-user').reset();
// }

// const send = function(ev){
//     ev.preventDefault();
//     ev.stopPropagation();

//     let fails = validate();

//     if(fails.length===0){
//         //good
//         document.getElementById('form-user').submit();
//     }
//     else{
//         //bad
//         fails.forEach(function(obj){
//             let field = document.getElementById(obj.input);
//             field.parentElement.classList.add('error');
//             field.parentElement.setAttribute('data-errormsg', obj.msg);
//         })
//     }
// }

// const validate = function(ev){

//     let failures = [];
//     let gallons = document.getElementById("input-gallons"); // extract gallons entry
//     var gal_Value = gallons.value;
//     let address = document.getElementById("input-address"); // extract address
//     if(gal_Value < 0){
//         failures.push({input:'input-gallons', msg:'not enough'});
//     }
//     if(address.value === ""){
//         failures.push({input:'input-address',msg:'Required Field'});
//     }
//     return failures;
// }

//document.addEventListener('DOMContentLoaded',init);

// -----------
// let gallonsValue, addressValue, dateValue;

// document.querySelector('#input-gallons-input').value = 0;
// const submit = document.querySelector('#button-send');

// submit.addEventListener('click', function(e) {
//     e.preventDefault();
  
//     let gallonsInput = document.querySelector('#input-gallons-input').value;
//     let dateInput = document.querySelector('#input-date-input').value; 
//     if (gallonsInput < 1)
//     {
//         alert('Please input valid number of gallons');
//         return;
//     }
//     else if (dateInput == "")
//     {
//         alert('Please select a delivery date');
//     }
//     else
//     {
//         gallonsValue = gallonsInput;    // load inputs
//         addressValue = document.querySelector('#input-address-input').value;
//         dateValue = document.querySelector('#input-date-input').value;

//         let suggestedPrice = 9.99; // HARDCODED VALUE: REPLACE
//         let totalDue = 99.90 // HARDCODED VALUE: REPLACE

//         alert(`Suggested Price: ${suggestedPrice}
//         Total Amount Due: ${totalDue}`);

//         let historyRedirect = 'http://' + window.location.host + '/history';
//         window.location.href = historyRedirect;
//     }
// })

const getQuote = document.querySelector('#getQuote');
const form = document.querySelector('#form-user');

getQuote.addEventListener('click', function(e) {
    e.preventDefault();

    let deliveryDateValue = document.querySelector('#id_deliveryDate').value;
    let gallonsReqValue = document.querySelector('#id_gallonsReq').value;
    if (deliveryDateValue == '' || gallonsReqValue == '')
        alert('You must enter number of gallons AND delivery date.');
    else
    {
        let priceValue = 1.50; // HARDCODED, APPLY PRICING MODULE HERE

        // function getPriceValue(){
        //     $.ajax({
        //         url: "/form",
        //         type: "POST",
        //         dataType: "json",
        //         success: function(data){
        //             $(test).replaceWith
        //         }
        //     });
        // }
        
        document.querySelector('#price').value = priceValue; 
        document.querySelector('#total').value = gallonsReqValue * priceValue;
    }
})

