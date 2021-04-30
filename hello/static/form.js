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
        let basePrice = 1.50;
        let state = document.querySelector('#state').textContent;
        let ratehistory = document.querySelector('#ratehistory').textContent;
        let location_factor, rate_history_factor, gallons_requested_factor;

        if(state == "TX") {
            location_factor = 0.020;
        }
        else {
            location_factor = 0.040;
        }

        if(ratehistory == "True") {
            rate_history_factor = 0.010;
        }
        else {
            rate_history_factor = 0.000;
        }

        if(gallonsReqValue >= 1000) {
            gallons_requested_factor = 0.020
        }
        else {
            gallons_requested_factor = 0.030
        }
        let margin = basePrice * (location_factor - rate_history_factor + gallons_requested_factor + 0.100);
        let suggestedPrice = basePrice + margin;
        let totalPrice = suggestedPrice * gallonsReqValue;

        
        document.querySelector('#price').value = suggestedPrice; 
        document.querySelector('#total').value = totalPrice;
    }
})

