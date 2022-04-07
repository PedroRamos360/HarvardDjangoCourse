function handleImageChange(event) {
    const file = event.target.files[0];
    const fileReader = new FileReader();
    fileReader.onloadend = function () {
        var img = document.querySelector('.previewimage');
        img.src = fileReader.result;
        img.hidden = false;
        var form = document.querySelector('.clothingform');
        form.style.height = '500px';
        form.style.margin = '0 0 80px 0';
    }
    fileReader.readAsDataURL(file);
}