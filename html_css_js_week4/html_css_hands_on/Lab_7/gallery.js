document.addEventListener("DOMContentLoaded", function () {
  var modalEl = document.getElementById("galleryModal");
  if (!modalEl) return;
  var modal = new bootstrap.Modal(modalEl);
  var modalImg = document.getElementById("modalImage");
  var modalCaption = document.getElementById("modalCaption");

  document.querySelectorAll(".gallery-link").forEach(function (el) {
    el.addEventListener("click", function (ev) {
      ev.preventDefault();
      var src =
        el.getAttribute("data-src") ||
        (el.querySelector("img") && el.querySelector("img").src);
      var cap =
        el.getAttribute("data-caption") ||
        (el.querySelector("img") && el.querySelector("img").alt) ||
        "";
      if (src) {
        modalImg.src = src;
        modalImg.alt = cap;
      }
      modalCaption.textContent = cap;
      modal.show();
    });

    el.addEventListener("keydown", function (ev) {
      if (ev.key === "Enter" || ev.key === " ") {
        ev.preventDefault();
        el.click();
      }
    });
  });
});
