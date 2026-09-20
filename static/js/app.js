
document.addEventListener("DOMContentLoaded", () => {
  document.querySelectorAll(".upload-box input[type=file]").forEach(input => {
    input.addEventListener("change", () => {
      const box = input.closest(".upload-box");
      if (input.files && input.files[0]) {
        box.querySelector("strong").textContent = input.files[0].name;
      }
    });
  });
});
function showToast(message) {
  const toast = document.createElement("div");
  toast.className = "toast";
  toast.textContent = message;
  document.body.appendChild(toast);
  setTimeout(() => toast.remove(), 2600);
}

function showRewardTab(tab, button) {
  document.querySelectorAll(".tabs button").forEach(b => b.classList.remove("selected"));
  button.classList.add("selected");
  const history = document.getElementById("reward-history");
  const redeem = document.getElementById("reward-redeem");
  if (history && redeem) {
    history.style.display = tab === "history" ? "" : "none";
    redeem.style.display = tab === "redeem" ? "" : "none";
  }
}
document.addEventListener("click", (event) => {
  const target = event.target.closest("[data-demo]");
  if (target) {
    event.preventDefault();
    showToast(target.getAttribute("data-demo"));
  }
});


function togglePassword(button){
  const input = button.parentElement.querySelector('input');
  if(!input) return;
  input.type = input.type === 'password' ? 'text' : 'password';
  button.textContent = input.type === 'password' ? '◉' : '◌';
}
