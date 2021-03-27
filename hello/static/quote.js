const quoteOk = document.querySelector('#quoteOk')

quoteOk.addEventListener('click', function(e) {
    let historyRedirect = 'http://' + window.location.host + '/history';
    window.location.href = historyRedirect;
})