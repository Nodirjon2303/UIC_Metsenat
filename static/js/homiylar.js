"use strict";

const closeFilter = document.querySelector("#filter_close");
const showFilter = document.querySelector(".main__btn");
const filter = document.querySelector(".filter_box");

showFilter.addEventListener("click", () => {
    filter.classList.add("show");
});

closeFilter.addEventListener("click", () => {
    filter.classList.remove("show");
});


function homiy_search() {
    var search = document.getElementById('homiysearch').value
    var url = `/main/homiysearch/`;
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
                    <th>Tel.Raqami</th>
                    <th>Homiylik summasi</th>
                    <th>Sarflangan summa</th>
                    <th>Sana</th>
                    <th>Holati</th>
                    <th>amallar</th>
                </tr>`
                    for (var i = 0; i < data.length; i++) {
                        html += `<tr>
                        <td>${data[i].N}</td>
                        <td>${data[i].fish}</td>
                        <td>+998 ${data[i].phone}</td>
                        <td>${data[i].amount} <span>UZS</span></td>
                        <td>${data[i].spent} <span>UZS</span></td>
                        <td>${data[i].date}</td>
                        <td>${data[i].status}</td>
                        <td>
                            <a href="/main/singlehomiy/${data[i].id}/"
                            ><img src="/static/img/eye.png" alt="eye"
                            /></a>
                        </td>
                    </tr>`

                    }
                    document.getElementById('homiy_block').innerHTML=html;
                }
            })
        })
}