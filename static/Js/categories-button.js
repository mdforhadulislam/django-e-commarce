const menubutton = document.querySelector(".all-categories-button");

menubutton.addEventListener("click", () => {
  const nav = document.querySelector(".all-categories");
  console.log(nav);
  const AllclassList = nav.classList;
  for (let i = 0; AllclassList.length > i; i++) {
    if (AllclassList[i] === "hidden") {
      nav.classList.remove("hidden");
      nav.classList.add("show");
      return null;
    } else if (AllclassList[i] === "show") {
      nav.classList.remove("show");
      nav.classList.add("hidden");
      return null;
    }
  }
});
