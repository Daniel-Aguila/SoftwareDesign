const init = function(){
    document.getElementById('button-cancel').addEventListener('click',reset);
    document.getElementById('button-send').addEventListener('click',send);
}

const reset = function(ev){
    ev.preventDefault();
    document.getElementById('form-user').reset();
}

const send = function(ev){
    ev.preventDefault();
    ev.stopPropagation();

    let ret = validate();

    if(ret){
        //good
        document.getElementById('form-user').submit();
    }
    else{
        //bad
    }
}

const validate = function(ev){}

document.addEventListener('DOMContentLoaded',init)