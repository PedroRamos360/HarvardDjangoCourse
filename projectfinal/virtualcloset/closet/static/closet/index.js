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

function handleClothingChange(event) {
    var img = document.querySelector('.previewimage');
    img.hidden = false;
}