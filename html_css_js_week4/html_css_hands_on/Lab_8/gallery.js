document.addEventListener("DOMContentLoaded", function () {
  var modalEl = document.getElementById("galleryModal");
  if (!modalEl) return;
  var modal = new bootstrap.Modal(modalEl);
  var img = document.getElementById("modalImage");
  var cap = document.getElementById("modalCaption");

  document.querySelectorAll(".gallery-link").forEach(function (a) {
    a.addEventListener("click", function (e) {
      e.preventDefault();
      img.src = a.getAttribute("data-src");
      cap.textContent = a.getAttribute("data-caption") || "";
      modal.show();
    });
  });
});
