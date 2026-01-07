let avatarInput = document.getElementById("avatarInput");
let avatarPreview = document.getElementById("avatarPreview");

avatarInput?.addEventListener("change", (e) => {
  let f = avatarInput.files[0];
  if (!f) return;
  let r = new FileReader();
  r.onload = () => (avatarPreview.src = r.result);
  r.readAsDataURL(f);
});

let addBtn = document.getElementById("addSkill");
let skillInput = document.getElementById("skillInput");
let skillsArea = document.getElementById("skillsArea");

function addSkill() {
  let v = skillInput.value.trim();
  if (!v) return;
  let b = document.createElement("span");
  b.className = "badge bg-secondary";
  b.innerHTML = v + " ";
  let x = document.createElement("span");
  x.innerHTML = "×";
  x.style.cursor = "pointer";
  x.onclick = () => b.remove();
  b.appendChild(x);
  skillsArea.appendChild(b);
  skillInput.value = "";
}
addBtn?.addEventListener("click", addSkill);
skillInput?.addEventListener("keydown", (e) => {
  if (e.key === "Enter") {
    e.preventDefault();
    addSkill();
  }
});
