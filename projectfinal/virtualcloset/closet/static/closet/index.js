function handleImageChange(event) {
    const file = event.target.files[0];
    const fileReader = new FileReader();
    fileReader.onloadend = function () {
        var img = document.querySelector('.previewimage');
        img.src = fileReader.result;
        img.hidden = false;
    }
    fileReader.readAsDataURL(file);
}
function handleImageChangeLook() {
    var strong = document.querySelector('.imagechoosen');
    var p = document.querySelector('.imagechoosenp');
    p.hidden = false;
    strong.hidden = false;
    var number = strong.innerHTML;
    number = parseInt(number);
    number += 1;
    strong.innerHTML = number;
}

function handleClothingChange() {
    var img = document.querySelector('.previewimage');
    img.hidden = false;
}