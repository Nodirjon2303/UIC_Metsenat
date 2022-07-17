"use strict";

const close = document.querySelector("#filter_close");
const ready = document.querySelector(".see");
const seeFilter = document.querySelector(".main__btn");
const filterBox = document.querySelector(".filter_box");

seeFilter.addEventListener("click", () => {
    filterBox.classList.add("show");
});

close.addEventListener("click", () => {
    filterBox.classList.remove("show");
});
ready.addEventListener("click", () => {
    filterBox.classList.remove("show");
});


function talaba_search() {
    var search = document.getElementById('talabasearch').value
    var url = `/main/talabasearch/`;
    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken,
        },
        body: JSON.stringify({
            'key': search
        })
    })
        .then((response) => {
            response.json().then((data) => {
                if (data['state'] == 'ok') {
                    data = data['data']
                    var html = `<tr>
              <th>#</th>
              <th>F.i.sh.</th>
              <th>Talabalik turi</th>
              <th>OTM</th>
              <th>Ajratilingan summa</th>
              <th>Kontrakt miqdori</th>
              <th>Amallar</th>
            </tr>`
                    for (var i = 0; i < data.length; i++) {
                        html += `<tr>
              <td>${data[i].N}</td>
              <td>${data[i].fish}</td>
              <td>${data[i].turi}</td>
              <td>${data[i].otm}</td>
              <td>${data[i].homiy_amount} <span>UZS</span></td>
              <td>${data[i].kontrakt} <span>UZS</span></td>
              <td>
                <a href="/main/single-student/${data[i].id}/"
                  ><img src="/static/img/eye.png/" alt="eye"
                /></a>
              </td>
            </tr>`

                    }
                    document.getElementById('homiy_block').innerHTML = html;
                }
            })
        })
}
