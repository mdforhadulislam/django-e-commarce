const header = document.querySelector(".header");

window.addEventListener("scroll", () => {
  if (window.scrollY > 300) {
    header.classList.add("fixed");
    header.classList.add("shadow-md");
  } else {
    header.classList.remove("fixed");
    header.classList.remove("shadow-md");
  }
});

const upbutton = document.querySelector(".upbutton");

window.addEventListener("scroll", () => {
  if (window.scrollY > 300) {
    upbutton.style.display = "block";
  } else {
    upbutton.style.display = "none";
  }
});
