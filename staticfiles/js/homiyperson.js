"use strict";

const edit = document.querySelector(".card_edit");
const box = document.querySelector(".edit_back");
const close = document.querySelector(".edit_close");

edit.addEventListener("click", () => {
    box.classList.add("show");
});

close.addEventListener("click", () => {
    box.classList.remove("show");
});

function change_active(element) {
    if (element == `jismoniy`) {
        document.getElementById('yuridik').classList.remove('active')
        document.getElementById('community').style.display="none";
    } else {
        document.getElementById('jismoniy').classList.remove('active')
        try {
            document.getElementById('community').style.display = "inline";
        }
        catch(e){
            document.getElementById('communitydiv').innerHTML = `<div id="community" >
                            <label for="community">Tashkilot Nomi</label>
                            <input
                                    type="text" class="active"
                                    name="community"
                                    value=""
                                    placeholder="Tashkilot nomini kiriting"
                            />
                            <br>
                            </div>`
        }
        }
    document.getElementById(`${element}`).classList.add("active");
    document.getElementById("typeshaxs").value = element;
}
