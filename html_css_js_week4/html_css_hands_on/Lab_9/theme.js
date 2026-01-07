(function () {
  var btn = document.getElementById("themeToggle");
  if (!btn) return;

  var mode = localStorage.getItem("theme") || "light";
  if (mode === "dark") document.body.classList.add("dark");

  btn.addEventListener("click", function () {
    document.body.classList.toggle("dark");
    localStorage.setItem(
      "theme",
      document.body.classList.contains("dark") ? "dark" : "light"
    );
  });
})();
