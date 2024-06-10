if (document.getElementById("tryButton") != null) {
  document.getElementById("tryButton").addEventListener("click", function() {
      window.location.href = "/create";
    });
}

dropdown_items = document.getElementsByClassName("dropdown-item");

for (var i = 0; i < dropdown_items.length; i++) {

  dropdown_items[i].addEventListener("click", function() {
      document.getElementById("chooseCategory").innerHTML = this.innerHTML;
      let target = this.innerHTML.toLowerCase();
      fetch("http://127.0.0.1:1337/get-items?target=" + target)
                .then(response => {
                    if (!response.ok) {
                        throw new Error('Network response was not ok ' + response.statusText);
                    }
                    return response.text();
                })
                .then(data => {
                    document.getElementById("optionsSpace").innerHTML = data;
                })
                .catch(error => {
                    console.error('There was a problem with the fetch operation:', error);
                });
  });
}

function SelectItem(path, thisItem) {
  document.cookie = "selection=" + path + "; sameSite=Strict;";
  items = document.getElementsByClassName("option-item");
  for (var i = 0; i < items.length; i++) {
    items[i].style.boxShadow = "none";
  }
  thisItem.style.boxShadow = "0px 0px 10px 2px #03DAC6";

}

function add() {
  if (document.cookie.split("selection=")[1].length == 0) {
    alert("Please select an item before pressing add.");
  }
  var selection = document.cookie.split("selection=")[1];
  var sitePieces = JSON.parse(document.cookie.split("site-pieces=")[1].split(";")[0]);
  sitePieces.push(selection);
  document.cookie = "site-pieces=" + JSON.stringify(sitePieces) + "; sameSite=Strict;";
  document.cookie = "selection=; sameSite=Strict;";

  alert("Item added to site!");
  items = document.getElementsByClassName("option-item");
  for (var i = 0; i < items.length; i++) {
    items[i].style.boxShadow = "none";
  }
}

