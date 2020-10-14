/* Project specific Javascript goes here. */

function customSubmit() {
    const checkForm = document.getElementById('voteForm');
    checkForm.submit();
}

const votePlus = document.getElementById('id_value_0');
const voteMinus = document.getElementById('id_value_1');

voteMinus.addEventListener('click', customSubmit);
votePlus.addEventListener('click', customSubmit);
