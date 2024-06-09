if (document.getElementById("tryButton") != null) {
  document.getElementById("tryButton").addEventListener("click", function() {
      window.location.href = "/create";
    });
}

dropdown_items = document.getElementsByClassName("dropdown-item");

for (var i = 0; i < dropdown_items.length; i++) {

  dropdown_items[i].addEventListener("click", function() {
      document.getElementById("chooseCategory").innerHTML = this.innerHTML;
  });
}