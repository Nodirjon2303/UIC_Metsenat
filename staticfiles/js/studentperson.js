"use strict";

const edit = document.querySelector(".card_edit");
const box = document.querySelector(".edit_back");
const close = document.querySelector(".edit_close");
const closeHomiy = document.querySelector(".edit_close-homiy");
const addHomiyBtn = document.querySelector(".add_homiy_btn");
const addHomiy = document.querySelector(".add_homiy");

edit.addEventListener("click", () => {
    box.classList.add("show");
});

close.addEventListener("click", () => {
    box.classList.remove("show");
});
closeHomiy.addEventListener("click", () => {
    addHomiy.classList.remove("show");
});
console.log(addHomiy);
addHomiyBtn.addEventListener("click", () => {
    addHomiy.classList.add("show");
});


function homiy_balance() {
    var homiy_id = document.getElementById('homiyism').value;
    var url = `/main/checkbalance/`;
    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken,
        },
        body: JSON.stringify({
            'homiy_id': homiy_id
        })
    })
        .then((response) => {
            response.json().then((data) => {
                if (data['data'] == 'ok') {
                    document.getElementById("homiyamount").max = `${data['balance']}`
                    document.getElementById('homiyamount').placeholder = `${data['balance']} so'mgacha kiriting `
                }
            })
        })
}