document.addEventListener("DOMContentLoaded", function () {
  var container2 = document.getElementById("container2"); // Cambiado a document.getElementById("container2")
  var averagePercentage =
    parseFloat(document.getElementById("average_percentage").innerText) / 100; // Convert percentage to decimal
  console.log(document.getElementById("average_percentage").innerText);
  var bar = new ProgressBar.Circle(container2, {
    color: "#2000fb",
    strokeWidth: 4,
    trailWidth: 6,
    trailColor: "#fff",
    easing: "easeInOut",
    duration: 1400,
    text: {
      autoStyleContainer: false,
    },
    from: { color: "#2000fb", width: 6 },
    to: { color: "#2000fb", width: 4 },
    step: function (state, circle) {
      circle.path.setAttribute("stroke", state.color);
      circle.path.setAttribute("stroke-width", state.width);

      var value = Math.round(circle.value() * 100);
      if (value === 0) {
        circle.setText("");
      } else {
        circle.setText(value + "%");
      }
    },
  });

  bar.text.style.fontFamily = '"Raleway", Helvetica, sans-serif';
  bar.text.style.fontSize = "1rem";

  bar.animate(averagePercentage); // Number from 0.0 to 1.0
});
