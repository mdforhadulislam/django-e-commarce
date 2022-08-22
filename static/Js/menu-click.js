const menu = document.querySelector(".menu-button");

menu.addEventListener("click", () => {
  const nav = document.querySelector(".menu-list");
  const AllclassList = nav.classList;
  for (let i = 0; AllclassList.length > i; i++) {
    if (AllclassList[i] === "menutoptobottom") {
      nav.classList.remove("menutoptobottom");
      nav.classList.add("menubottomtotop");
      return null;
    } else if (AllclassList[i] === "menubottomtotop") {
      nav.classList.remove("menubottomtotop");
      nav.classList.add("menutoptobottom");
      return null;
    }
  }
});
