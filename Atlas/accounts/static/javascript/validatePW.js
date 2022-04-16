let pass1 = document.querySelector('#password');
let pass2 = document.querySelector('#password1');
let result = document.querySelector('#text');
let button = document.querySelector("#button");

button.disabled = true;

var submit = document.getElementsByTagName('button')[0];

function checkPassword () {
    pass1.value === pass2.value ? button.disabled = false : button.disabled = true;
}


pass1.addEventListener('keyup', () => {
    if (pass2.value.length >= 8) {
        checkPassword();
    } else if (pass2.value.length < 8) {
        button.disabled = true;
    } else if (pass1.value.length >= 8) {
        checkPassword();
    } else if (pass1.value.length < 8) {
        button.disabled = true;
    }
})

pass2.addEventListener('keyup', checkPassword);
