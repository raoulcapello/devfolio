/* DevFolio specific Javascript */
document.querySelectorAll(".nav-link").forEach((item) => {
  item.addEventListener("click", () => {
    setTimeout(() => {
      document
        .querySelector("#navbarCollapseMainMenu")
        .classList.remove("show");
    }, 500);
  });
});
