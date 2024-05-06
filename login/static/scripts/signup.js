const idPassword1 = document.getElementById("id_password1"),
  idPassword2 = document.getElementById("id_password2"),
  icon = document.querySelector(".bx");

icon.addEventListener("click", (e) => {
  if (idPassword1.type === "password") {
    idPassword1.type = "text";
    idPassword2.type = "text";
    icon.classList.remove("bx-show-alt");
    icon.classList.add("bx-hide");
  } else {
    idPassword1.type = "password";
    idPassword2.type = "password";
    icon.classList.add("bx-show-alt");
    icon.classList.remove("bx-hide");
  }
});
