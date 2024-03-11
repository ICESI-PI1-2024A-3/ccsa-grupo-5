const id_password1 = document.getElementById("id_password1"),
  id_password2 = document.getElementById("id_password2"),
  icon = document.querySelector(".bx");

icon.addEventListener("click", (e) => {
  if (id_password1.type === "password") {
    id_password1.type = "text";
    id_password2.type = "text";
    icon.classList.remove("bx-show-alt");
    icon.classList.add("bx-hide");
  } else {
    id_password1.type = "password";
    id_password2.type = "password";
    icon.classList.add("bx-show-alt");
    icon.classList.remove("bx-hide");
  }
});
