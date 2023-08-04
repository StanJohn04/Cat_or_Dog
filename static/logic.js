function loadFile(event) {
    var image = document.getElementById('output');
    image.src = URL.createObjectURL(event.target.files[0]);
  };

function hide_output() {
    var x = document.getElementById("prediction");
    var y = document.getElementById("image_predicted")
    if (x.style.display === "none") {
      x.style.display = "block";
    } else {
      x.style.display = "none";
    }

    if(y.style.visibility === 'hidden'){
      y.style.visibility = 'visible'
    }
    else{
      y.style.visibility = 'hidden'
    }
};


var fileTag = document.getElementById("filetag"),
    preview = document.getElementById("preview");
    
fileTag.addEventListener("change", function() {
  changeImage(this);
});

function changeImage(input) {
  var reader;

  if (input.files && input.files[0]) {
    reader = new FileReader();

    reader.onload = function(e) {
      preview.setAttribute('src', e.target.result);
    }

    reader.readAsDataURL(input.files[0]);
  }
}