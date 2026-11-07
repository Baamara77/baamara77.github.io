const menuToggle = document.getElementById("menuToggle");
const navContent = document.getElementById("navContent");

if (menuToggle && navContent) {
  menuToggle.addEventListener("click", () => {
    const opened = navContent.classList.toggle("open");
    menuToggle.setAttribute("aria-expanded", String(opened));
  });

  navContent.querySelectorAll("a").forEach((link) => {
    link.addEventListener("click", () => {
      navContent.classList.remove("open");
      menuToggle.setAttribute("aria-expanded", "false");
    });
  });
}

const year = document.getElementById("year");
if (year) year.textContent = new Date().getFullYear();
