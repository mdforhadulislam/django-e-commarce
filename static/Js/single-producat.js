const color_box = document.querySelectorAll(".producat-number");
const incriment = document.querySelector(".incriment");
const decriment = document.querySelector(".decriment");

incriment.addEventListener("click", (e) => {
  e.target.parentElement.parentElement.parentElement.children[0].value;
  e.target.parentElement.parentElement.parentElement.children[0].value =
    Number(
      e.target.parentElement.parentElement.parentElement.children[0].value
    ) + 1;
});

decriment.addEventListener("click", (e) => {
  e.target.parentElement.parentElement.parentElement.children[0].value;
  if (
    Number(
      e.target.parentElement.parentElement.parentElement.children[0].value
    ) >= 1
  ) {
    e.target.parentElement.parentElement.parentElement.children[0].value =
      Number(
        e.target.parentElement.parentElement.parentElement.children[0].value
      ) - 1;
  }
});
