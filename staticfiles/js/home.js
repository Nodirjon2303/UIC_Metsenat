"use strict";

// const btnShow = document.querySelector(".btn-show");
// console.log(btnShow);
// const btnHide = document.querySelector(".btn-hide");
// const box = document.querySelector(".box");

// btnShow.addEventListener("click", () => {
//   box.classList.add("box2");
// });

// btnHide.addEventListener("click", () => {
//   box.classList.remove("box2");
// });

const jismoniy = document.querySelector("#jismoniy");
const yuridik = document.querySelector("#yuridik");
const yuridikRemove = document.querySelector(".yuridik-remove");
const priceBtn = document.querySelector(".price__btn");
const priceShow = document.querySelector("#pricecount");

jismoniy.addEventListener("click", () => {
  jismoniy.classList.add("active");
  yuridik.classList.remove("active");
  yuridikRemove.classList.remove("yuridik-remove-show");
  document.getElementById('cname').value = null;
});

yuridik.addEventListener("click", () => {
  jismoniy.classList.remove("active");
  yuridik.classList.add("active");

  yuridikRemove.classList.add("yuridik-remove-show");
});

priceBtn.addEventListener("click", () => {
  priceShow.classList.add("show");
});

function remove_summa(){
  priceShow.classList.remove("show")
  document.getElementById("pricecount").value = ''
}
