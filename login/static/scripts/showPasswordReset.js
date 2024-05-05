const passwordFields = document.querySelectorAll("input[type='password']"),
  icon = document.getElementById("togglePassword2");

icon.addEventListener("click", function () {
  passwordFields.forEach(function (field) {
    if (field.type === "password") {
      field.type = "text";
      icon.classList.remove("bx-hide");
      icon.classList.add("bx-show-alt");
    } else {
      field.type = "password";
      icon.classList.add("bx-hide");
      icon.classList.remove("bx-show-alt");
    }
  });
});
