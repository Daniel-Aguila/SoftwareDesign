const quoteContainer = document.querySelector('#quoteTable');

const dummyEntry = document.querySelector('#dummyEntry');
dummyEntry.addEventListener('click', function(e) { // EVENT WILL BE CHANGED FROM BUTTON PRESS TO AN ACTUAL SUBMISSION OF A FUEL QUOTE
    e.preventDefault();

    addEntry();
})

const addEntry = (/*entry*/) => { 

    // WILL EXTRACT VALUES FROM "entry", FOR NOW USING DUMMY VALUES
    let gallonsReqValue = 10;
    let addressValue = "9999 Santa Clara Ave. Schenectady, NY 12302";
    let dateValue = "01/01/2000";
    let ppgValue = 9.99;
    // WILL EXTRACT VALUES FROM "entry", FOR NOW USING DUMMY VALUES

    let totalDueValue = gallonsReqValue * ppgValue;
    totalDueValue = totalDueValue.toFixed(2);

    const tableRow = document.createElement('tr');

    const gallonsReq = document.createElement('td');
    const address = document.createElement('td');
    const date = document.createElement('td');
    const ppg = document.createElement('td');
    const totalDue = document.createElement('td');

    gallonsReq.append(gallonsReqValue);
    address.append(addressValue);
    date.append(dateValue);
    ppg.append(ppgValue);
    totalDue.append(totalDueValue);

    tableRow.append(gallonsReq);
    tableRow.append(address);
    tableRow.append(date);
    tableRow.append(ppg);
    tableRow.append(totalDue);


    quoteContainer.append(tableRow);
}