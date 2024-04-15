const passwordField = document.querySelector("input[name='password']"),
  icon = document.getElementById("togglePassword2");

icon.addEventListener("click", function () {
  if (passwordField.type === "password") {
    passwordField.type = "text";
    icon.classList.remove("bx-hide");
    icon.classList.add("bx-show-alt");
  } else {
    passwordField.type = "password";
    icon.classList.add("bx-hide");
    icon.classList.remove("bx-show-alt");
  }
});
